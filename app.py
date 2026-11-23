import streamlit as st
import zoner_audit as za

st.set_page_config(page_title="Zoner SEO + GEO audit", page_icon="🔎")
st.title("🔎 Zoner SEO + GEO audit")
st.caption("Paste 1-5 public zoner.fi page addresses. The tool checks them and proposes better Finnish copy. "
           "Nothing is published: you decide what to use.")

urls_text = st.text_area("Page addresses (one per line)", height=130,
                         placeholder="https://zoner.fi/\nhttps://zoner.fi/...")

if st.button("Run audit", type="primary"):
    urls = [u.strip() for u in urls_text.splitlines() if u.strip()]
    if not urls:
        st.warning("Paste at least one address first.")
    elif len(urls) > 5:
        st.warning("Please use at most 5 addresses at a time.")
    else:
        cache, results = {}, []
        bar = st.progress(0.0)
        for i, u in enumerate(urls):
            with st.spinner(f"Checking {u} ..."):
                results.append(za.run_url(u, cache))
            bar.progress((i + 1) / len(urls))
        for r in results:
            with st.expander(r["url"], expanded=True):
                if "error" in r:
                    st.error(r["error"])
                    continue
                for x in r["page"]["findings"]:
                    st.write(f"{za.ICON[x['level']]} **{x['area']}**: {x['msg']}")
                if "suggest_error" in r:
                    st.error("Proposal not created: " + r["suggest_error"])
                    continue
                s = r["suggestion"]
                st.subheader(f"Proposal - automatic check: {r['verdict']}")
                st.write(f"**Title:** {s.get('title','')}")
                st.write(f"**Meta:** {s.get('meta_description','')}")
                st.write(f"**H1:** {s.get('h1','')}")
                st.write("**Suggested H2 structure:**")
                for o in s.get("outline", []):
                    st.write("- " + o)
                st.write("**FAQ:**")
                for x in s.get("faq", []):
                    st.write(f"- **{x.get('q','')}** {x.get('a','')}")
                st.write("**Automatic checks:**")
                for c in r["checks"]:
                    st.write(f"{za.ICON[c['level']]} {c['msg']}")
                st.caption("A person must read the text before it is used.")
        st.download_button("Download report (HTML)", za.to_html(results), "zoner-report.html", "text/html")

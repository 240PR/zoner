# Setup (developer, 5 min)
```
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...        # Windows: set ANTHROPIC_API_KEY=...
streamlit run app.py                       # browser UI for the marketer
python zoner_audit.py urls.txt report.html # or command line
```
Optional: `ANTHROPIC_MODEL` (default claude-sonnet-5-5), `ZONER_ALLOW_ANY=1` to allow non-zoner.fi hosts.

Structure: `zoner_audit.py` = fetch -> audit (rules, no AI) -> suggest (Claude) -> check (rules) -> report.
Only public page text is sent to Claude; no customer data.
Pages are fetched once per run and the HTML is parsed with BeautifulSoup (no JavaScript rendering).
# Setup on GitHub (no installation needed)

1. Create a new **private** repository and upload all these files (including the hidden `.github` folder).
2. Settings > Secrets and variables > Actions > New repository secret. Name: `ANTHROPIC_API_KEY`, value: your key.
3. Actions tab > "Zoner SEO + GEO audit" > Run workflow > paste page addresses > Run.
4. Open the finished run: results table on the page, full report under **Artifacts**.

Never put the key in a file or in chat.

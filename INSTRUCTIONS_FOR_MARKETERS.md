# Zoner SEO + GEO audit: how to use it

**What it does:** you paste 1-5 public zoner.fi page addresses. It checks each page for SEO and GEO
(being found in Google and cited by ChatGPT, Gemini, AI Overviews), then proposes better Finnish copy
and checks that proposal automatically. **It never changes the website.**

## Starting it
1. Open the tool address your developer gave you (or double-click `start.command` / `start.bat`).
2. Paste the page addresses, one per line. Click **Run audit**.
3. Wait about 20-40 seconds per page.

## Reading the result
For each page you get:
- **Audit** - ✅ fine, ⚠️ could be better, ❌ a real problem.
- **Proposal** - a new title, meta description, H1, H2 structure and FAQ in Finnish.
- **Automatic check** - PASS / REVIEW / FAIL.
  - **FAIL**: do not use the text. Usually a price or claim that is not on the real page.
  - **REVIEW**: read the flagged lines and compare with the real page.
  - **PASS**: the automatic checks found nothing. **You still read it.** PASS does not mean the text is good.

Click **Download report** to save everything as one file you can share.

## If something goes wrong
| You see | What it means | What to do |
|---|---|---|
| "is not a full web address" | The address is incomplete | Copy it again from the browser, starting with https:// |
| "is not a zoner.fi page" | Only zoner.fi pages are allowed | Use a zoner.fi address |
| "This page does not exist (404)" | Typo or page removed | Check the address in your browser |
| "The site refused the request" | Site is blocking the tool for now | Wait a few minutes; if it repeats, tell the developer |
| "took too long to answer" | Site is slow | Try again in a minute |
| "Only N words of text found" | The page loads content with JavaScript, the tool cannot see it | Treat results with caution; tell the developer |
| "No Claude API key is set" / "rejected the API key" | Setup problem | Tell the developer (not your fault) |
| "usage limit" / "Claude is busy" | Too many requests | Wait a minute, run fewer pages |
| "not in the expected format" | Claude answered oddly | Press Run audit again |

One failing page never stops the others.

## Rules
- Only public pages. Never paste customer data.
- A person always reads and approves the text before anything is used or published.

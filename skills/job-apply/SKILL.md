---
name: job-apply
description: Fill job applications using Chrome DevTools MCP — triggers Simplify extension first, then intelligently fills remaining fields from resume and project data.
---

# Job Application Filler

Automate job application filling using Chrome DevTools MCP tools. Uses the Simplify browser extension for initial auto-fill, then intelligently fills remaining fields from the user's resume and project descriptions.

## When to Activate

- User asks to fill a job application
- User provides a job application URL
- User is on a job application page and wants help completing it

## Prerequisites

- Chrome browser open with Chrome DevTools MCP connected
- Simplify browser extension installed in Chrome
- Profile data filled in:
  - `skills/job-apply/profile/resume.md` — personal info, education, experience, skills
  - `skills/job-apply/profile/projects.md` — project descriptions and reusable answer snippets

## Non-Negotiables

1. **NEVER click Submit/Apply buttons** — always stop before submission and ask the user to review
2. **NEVER auto-fill sensitive fields** (SSN, bank details, salary if user hasn't specified) — flag these for the user
3. **Always take a final screenshot** for user review before declaring done
4. **Read profile data fresh** every time — never rely on cached/remembered values
5. **ALWAYS trigger Simplify FIRST** — finding and clicking the Simplify autofill button is the #1 priority before any manual filling. Try multiple methods (screenshot, snapshot, evaluate_script) to locate it. Only skip if Simplify is genuinely not installed.
6. **NEVER upload a cover letter** unless the form explicitly marks it as required. If the cover letter field is optional, leave it empty.

## Workflow

### Step 1: Load Profile Data

Read profile files to have all user data available:
- Read `skills/job-apply/profile/resume.md` for structured data (name, email, education, experience, skills)
- Read `skills/job-apply/profile/projects.md` for project summaries and reusable answer snippets
- For open-ended questions requiring detailed answers, read the relevant individual project file:
  - `skills/job-apply/profile/roma_project.md` — ROMA recursive deep search agent
  - `skills/job-apply/profile/sera_project.md` — SERA semantic embedding agent (detailed experiments + metrics)
  - `skills/job-apply/profile/multimodal_roma_project.md` — m-ROMA multimodal extension
  - `skills/job-apply/profile/strategy_deep_research.md` — Multi-agent deep research at Strategy
  - `skills/job-apply/profile/txt2sql_project.md` — Text2SQL agent at Piramal

If profile files are empty/incomplete, warn the user and ask them to fill in the data first.

### Step 2: Navigate to Application

If the user provides a URL:
```
Use mcp__chrome-devtools__navigate_page to go to the URL (timeout: 30000ms)
```

If the user says they're already on the page:
```
Use mcp__chrome-devtools__take_screenshot to see the current state
```

### Step 3: Trigger Simplify Extension

Simplify adds a floating button overlay to job application pages. Find and click it:

1. **Take a screenshot** to locate the Simplify button
   - Look for a blue/green floating button, often in the bottom-right corner
   - It may say "Autofill" or show the Simplify logo
   - Common selectors: `[class*="simplify"]`, `[id*="simplify"]`, `button` with Simplify text

2. **Click the Simplify button**:
   ```
   Use mcp__chrome-devtools__click with the Simplify button's location
   ```

3. **Wait for Simplify to populate fields**:
   ```
   Use mcp__chrome-devtools__wait_for with timeout of 5000ms for form fields to be filled
   ```

4. If Simplify button is not found, skip to Step 4 (manual fill all fields)

5. If Simplify opens a modal/popup, interact with it to confirm auto-fill

### Step 4: Screenshot & Analyze Gaps

After Simplify runs (or if skipped):

1. **Take a screenshot** of the full form
   ```
   Use mcp__chrome-devtools__take_screenshot
   ```

2. **Scroll down and take additional screenshots** if the form is long
   ```
   Use mcp__chrome-devtools__press_key with "PageDown" then screenshot again
   Repeat until you've seen the entire form
   ```

3. **Identify unfilled fields** by analyzing the screenshots:
   - Empty text inputs (no value visible)
   - Unselected dropdowns (showing "Select..." or placeholder)
   - Unchecked required checkboxes
   - Empty textareas (especially for open-ended questions)
   - File upload fields without files attached

### Step 5: Fill Remaining Fields

For each unfilled field, match it to profile data and fill:

#### Text Inputs (name, email, phone, LinkedIn, etc.)
```
Use mcp__chrome-devtools__click on the field first
Use mcp__chrome-devtools__fill with the value from resume.md
```

#### Dropdowns (work authorization, degree type, etc.)
```
Use mcp__chrome-devtools__click to open the dropdown
Use mcp__chrome-devtools__take_screenshot to see options
Use mcp__chrome-devtools__click on the correct option
```

#### Textareas (cover letter, "why this role", project descriptions)
```
Use mcp__chrome-devtools__click on the textarea
Use mcp__chrome-devtools__fill with content adapted from projects.md
```

For open-ended questions, follow these strict rules:
- **Plain simple English** — no jargon-heavy sentences, no filler words, no fluff
- **Under 150 words** — be short, crisp, and impactful. Every sentence must earn its place
- **Lead with the result** — start with what you achieved, then briefly explain how
- **One project per answer** — pick the single most relevant project from projects.md, don't cram multiple
- **Use real numbers** — percentages, dollar amounts, team sizes, time saved
- **No generic statements** — every answer must reference a specific project, tool, or metric from the profile
- **Read the question carefully** — answer exactly what's asked, nothing more
- Read the individual project files (roma_project.md, sera_project.md, etc.) for detailed context when composing answers

#### File Uploads (resume PDF, cover letter)
```
Use mcp__chrome-devtools__upload_file with the path from resume.md "Resume PDF Path" field
```

#### Checkboxes / Radio Buttons
```
Use mcp__chrome-devtools__click on the appropriate option
```

#### Field Matching Guide

| Form Label Pattern | Profile Source |
|---|---|
| First Name, Last Name, Full Name | resume.md > Personal Information > Full Name |
| Email, E-mail | resume.md > Personal Information > Email |
| Phone, Mobile, Telephone | resume.md > Personal Information > Phone |
| LinkedIn, LinkedIn URL | resume.md > Personal Information > LinkedIn |
| GitHub, Portfolio, Website | resume.md > Personal Information > GitHub/Portfolio |
| City, Location, Address | resume.md > Personal Information > Location |
| University, School, College | resume.md > Education > University |
| Degree, Education Level | resume.md > Education > Degree |
| Major, Field of Study | resume.md > Education > Major |
| GPA | resume.md > Education > GPA |
| Graduation Date, Grad Year | resume.md > Education > Graduation Date |
| Current Company, Employer | resume.md > Work Experience > Experience 1 > Company |
| Current Title, Job Title | resume.md > Work Experience > Experience 1 > Title |
| Years of Experience | resume.md > Additional Information > Years of Experience |
| Work Authorization, Legally authorized | resume.md > Work Authorization |
| Visa Sponsorship, Require sponsorship | resume.md > Work Authorization > Visa sponsorship required |
| Salary, Compensation, Pay | Flag for user -- do not auto-fill unless specified in resume.md |
| Start Date, Available from | resume.md > Additional Information > Earliest Start Date |
| How did you hear about us, Referral | resume.md > Additional Information > How did you hear about us |
| Gender, Race, Ethnicity, Veteran, Disability | resume.md > Additional Information (EEO fields -- use values if provided, otherwise select "Decline to self-identify") |
| Resume, CV (file upload) | resume.md > Resume PDF Path |
| Cover Letter (file upload) | resume.md > Cover Letter PDF Path |
| Tell us about yourself, Why interested, Describe a project | projects.md > select most relevant snippet and adapt |

### Step 6: Handle Platform-Specific Quirks

#### Greenhouse
- Multi-page forms: after filling visible fields, look for "Next" or "Continue" button
- Click it and repeat Steps 4-5 for the next page
- Custom questions often appear on page 2+

#### Lever
- Single-page forms with sections
- Resume upload is usually at the top
- Custom questions at the bottom

#### Workday
- Complex multi-step wizard
- Requires account creation sometimes -- flag for user
- Many dropdown-heavy fields

#### Ashby
- Clean single-page layout
- File upload then form fields

#### Generic ATS / Custom Forms
- Use screenshot analysis to identify form structure
- Match labels to profile data using the field matching guide above

### Step 7: Final Review

1. **Scroll to top** of the form
2. **Take screenshots** of every section of the completed form
3. **Present a summary** to the user:

```
## Application Review

**Company**: [from page title/header]
**Position**: [from page title/header]

### Fields Filled:
- First Name: [value]
- Last Name: [value]
- Email: [value]
- ...

### Fields Flagged for Review:
- Salary Expectation: [not filled -- needs your input]
- Custom Question: "Why do you want to work here?" [filled with adapted answer -- please review]

### Fields Not Found / Skipped:
- [any fields that couldn't be matched]

**Please review the screenshots above and submit manually when ready.**
```

4. **STOP HERE** -- do not click submit

## Handling Edge Cases

### CAPTCHA
- Flag for user: "There's a CAPTCHA on this form. Please solve it manually, then tell me to continue."

### Login Required
- Flag for user: "This application requires login. Please log in first, then tell me to continue."

### Multi-page Forms
- Fill each page completely before advancing
- Take screenshots of each page for the review summary

### Dynamic Fields (fields that appear based on previous answers)
- After filling a field that might trigger new fields, take a screenshot
- If new fields appeared, fill those too

### Pre-filled but Incorrect Fields
- If Simplify filled a field incorrectly, clear it first:
  ```
  Use mcp__chrome-devtools__click on the field (triple-click to select all)
  Use mcp__chrome-devtools__fill with the correct value
  ```

## Example Usage

```bash
# Fill a Greenhouse application
/job-apply https://job-boards.greenhouse.io/company/jobs/12345

# Fill the application currently open in Chrome
/job-apply

# Fill with specific notes
/job-apply https://lever.co/company/apply --note "Mention my ML experience for this role"
```

## Troubleshooting

| Issue | Solution |
|---|---|
| Simplify button not found | Skip Simplify, fill all fields manually from profile data |
| Chrome DevTools not connected | Ask user to ensure Chrome is open and MCP server is running |
| Field won't accept input | Try clicking the field first, then use `type_text` instead of `fill` |
| Dropdown options not visible | Take screenshot after clicking, use `press_key` with arrow keys to navigate |
| Form has iframes | Use `evaluate_script` to check for iframes, switch context if needed |
| File upload fails | Verify the PDF path in resume.md is correct and file exists |

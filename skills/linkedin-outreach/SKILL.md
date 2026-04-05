---
name: linkedin-outreach
description: Draft personalized LinkedIn outreach messages by researching the person/company from a LinkedIn post URL. Generates short, high-response-rate messages tailored for job seekers reaching out to hiring managers.
---

# LinkedIn Outreach Message Drafter

Draft personalized LinkedIn outreach messages that maximize response rates. Takes a LinkedIn post URL, researches the person and company, then generates a concise 3-paragraph message.

## When to Activate

- User shares a LinkedIn post URL and wants to reach out
- User wants to message a hiring manager, recruiter, or team lead about a role
- User asks to draft a LinkedIn connection request or InMail

## Profile Data

Read the user's profile from these files before drafting:
- `~/.claude/skills/job-apply/profile/resume.md` — personal info, experience, skills
- `~/.claude/skills/job-apply/profile/projects.md` — project summaries for matching relevance

## Workflow

### Step 1: Research the Target

Use `WebFetch` on the LinkedIn post URL to extract:
- **Who posted**: name, title, company
- **What the post is about**: job opening, company news, product launch, thought leadership
- **Company details**: what they do, industry, stage, size
- **Role details**: if hiring, what skills/qualities they want

If the post doesn't have enough info, use `WebSearch` to research:
- The company (what they build, recent news, funding, mission)
- The person (their role, background, what they care about)

### Step 2: Find the Connection

From the user's profile, identify the **single strongest overlap** between:
- User's experience/projects and what the company does
- User's skills and what the role needs
- User's interests and what the person posted about

Pick ONE specific thing — not a laundry list.

### Step 3: Draft the Message

Write a 3-paragraph LinkedIn message following these rules:

#### Structure

**Paragraph 1 — Hook + About Me (2-3 sentences)**
- Open by referencing their specific post/role (shows you did your homework)
- One sentence on who you are and your most relevant achievement
- Must feel personal, not templated

**Paragraph 2 — Why I'm a Good Fit (2-3 sentences)**
- Connect ONE specific project/skill to what they need
- Use a concrete metric or result (not vague claims)
- Show you understand their problem space

**Paragraph 3 — Soft Ask (1 sentence)**
- Low-pressure ask for a quick chat
- Give them an easy out so it doesn't feel transactional

#### Rules

- **Total length: 80-120 words max** — shorter messages get higher response rates
- **Plain simple English** — no corporate jargon, no buzzword soup
- **No flattery** — don't say "I love your company" or "your post was amazing"
- **No desperation** — don't say "I would be honored" or "it would mean the world"
- **Specific over generic** — reference their actual post content, not vague praise
- **One ask only** — don't ask for a referral AND a chat AND feedback
- **No resume dump** — pick one achievement, not five
- **Conversational tone** — write like a human, not a cover letter
- **No emojis** — keep it professional but warm

#### What NOT to write

BAD: "Hi! I came across your post and was really impressed by SmarterDx's work in healthcare AI. I'm a passionate ML engineer with 3+ years of experience in NLP, RAG, LLMs, and deep learning..."

GOOD: "Hi [Name] — saw your post about the Staff ML Engineer role at SmarterDx. I've been building production AI agents at Sentient, most recently a search agent that beat SOTA by 10% on hierarchical tasks."

### Step 4: Output to Markdown File

Write all results to an output markdown file (e.g., `outreach_messages.md` or a name the user specifies).

The file must have:
1. A **summary table** at the top with all posts
2. **Individual sections** below with the full drafted message for each post

#### Output Format

```markdown
# LinkedIn Outreach Messages

Generated: [date]

## Summary

The summary table must be comprehensive — it should contain ALL context (post link, location, who to message, why I'm a fit, flags) so the user can understand everything from the table alone without reading individual sections.

| # | Company | Role | Location | Person to Message | Post | Why I'm a Fit | Flags |
|---|---------|------|----------|-------------------|------|---------------|-------|
| 1 | [[Company]](#1-company--role) | [Role] | [City/Remote] | [Name, Title] | [post](url) | [specific match — reference projects/metrics] | [concerns or —] |
| 2 | ... | ... | ... | ... | ... | ... | ... |

The Company column links to the message section below (anchor format: `#1-company--role` using lowercase, hyphens, no special chars).

---

## 1. [Company] — [Role]

> Hi [Name] — saw your post about the [Role] at [Company]. I'm currently building
> [specific thing] at [Company], where I [specific result with metric].
>
> [Company]'s work on [specific thing from post] is close to what I did at [previous
> company] — I [specific achievement that maps to their need].
>
> Would you be open to a quick chat about the role?

---

## 2. [Company] — [Role]
...
```

Individual message sections contain ONLY the heading and the quoted message — no post link, match, or flags (those are already in the summary table).

If a post should be skipped (e.g., wrong location, unrelated role), still include it in the summary table with the reason in the Flags column, and write "**Skipped** — [reason]" in the message section.

## Adapting to Post Types

| Post Type | Approach |
|-----------|----------|
| **Job posting** | Reference the specific role, match your skills to their requirements |
| **Company news/milestone** | Congratulate briefly, connect your work to their growth area |
| **Thought leadership** | Reference their specific point, share a related experience |
| **Product launch** | Connect your experience to the problem their product solves |

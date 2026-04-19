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

- `Notion (fetch via `python3 scripts/notion/page_reader.py resume`)` — personal info, experience, skills
- `Notion (fetch via `python3 scripts/notion/page_reader.py projects`)` — project summaries for matching relevance

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

### Step 1.5: Classify Contact Type

Determine who you're messaging — this changes the message framework:

| Type               | Who                                         | Message Focus                                     |
| ------------------ | ------------------------------------------- | ------------------------------------------------- |
| **Recruiter**      | Talent acquisition, sourcing                | Fit criteria → screening answers → CTA            |
| **Hiring Manager** | Team lead who's hiring                      | Specific challenge → quantified achievement → ask |
| **Peer**           | Someone in a similar role on the team       | Genuine interest → shared problem → soft ask      |
| **Interviewer**    | Someone who will interview you (date known) | Research signal → connection → looking forward    |

**Key rule for Peer outreach:** Do NOT ask for a job. The referral happens naturally if the conversation flows. Lead with genuine interest in their work.

**Key rule for Interviewer outreach:** Keep it light. The goal is they know you prepared, not that you're desperate.

### Step 2: Find the Connection

From the user's profile, identify the **single strongest overlap** between:

- User's experience/projects and what the company does
- User's skills and what the role needs
- User's interests and what the person posted about

Pick ONE specific thing — not a laundry list.

### Step 3: Draft the Message

Write a 3-paragraph LinkedIn message following these rules:

#### Structure by Contact Type

**For Recruiters (3 sentences):**

1. **Fit:** Direct match criteria — role, relevant experience, availability/location
2. **Proof:** Answer their screening questions before they ask ("3+ years building ML pipelines, MS in ML from UMD, available June 2026")
3. **CTA:** "Happy to share my CV if this aligns with what you're looking for"

**For Hiring Managers (3 sentences):**

1. **Hook:** Specific challenge their team faces (from JD, company blog, or news)
2. **Proof:** Your biggest quantified achievement that shows you've solved similar problems
3. **CTA:** "Would love to hear how your team is approaching [specific challenge]"

**For Peers — referral (3 sentences):**

1. **Interest:** Genuine reference to their work — blog post, talk, open-source project, paper
2. **Connection:** Something you're doing in the same space (NOT a job pitch)
3. **CTA:** "I've been working on similar problems at [company], would love to hear your take on [topic]"

**For Interviewers — pre-interview (3 sentences):**

1. **Research:** Reference something specific about their work or background
2. **Context:** Light connection to your experience in that area
3. **CTA:** "Looking forward to our conversation on [date]"

**Generic (when type is unclear):**

**Sentence 1 — Hook + About Me**

- Reference their specific post/role (shows homework)
- One sentence on who you are + most relevant achievement

**Sentence 2 — Why I'm a Fit**

- Connect ONE specific project/skill to what they need
- Use a concrete metric (not vague claims)

**Sentence 3 — Soft Ask**

- Low-pressure ask for a quick chat
- Easy out so it doesn't feel transactional

#### Rules

- **Connection request: max 300 characters** (LinkedIn limit for connection notes)
- **InMail/message: 80-120 words max** — shorter messages get higher response rates
- **Plain simple English** — no corporate jargon, no buzzword soup
- **No flattery** — don't say "I love your company" or "your post was amazing"
- **No desperation** — don't say "I would be honored" or "it would mean the world"
- **Specific over generic** — reference their actual post content, not vague praise
- **One ask only** — don't ask for a referral AND a chat AND feedback
- **No resume dump** — pick one achievement, not five
- **Conversational tone** — write like a human, not a cover letter
- **No emojis** — keep it professional but warm
- **Never share phone number** in the message
- **Suggest alternative targets** — if primary contact doesn't respond, suggest 1-2 backup contacts with justification

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

| #   | Company                       | Role   | Location      | Person to Message | Post        | Why I'm a Fit                                 | Flags           |
| --- | ----------------------------- | ------ | ------------- | ----------------- | ----------- | --------------------------------------------- | --------------- |
| 1   | [[Company]](#1-company--role) | [Role] | [City/Remote] | [Name, Title]     | [post](url) | [specific match — reference projects/metrics] | [concerns or —] |
| 2   | ...                           | ...    | ...           | ...               | ...         | ...                                           | ...             |

The Company column links to the message section below (anchor format: `#1-company--role` using lowercase, hyphens, no special chars).

---

## 1. [Company] — [Role]

> Hi [Name] — saw your post about the [Role] at [Company]. I'm currently building
> [specific thing] at [Company], where I [specific result with metric].
>
> [Company]'s work on [specific thing from post] is close to what I did at [previous
>
> > company] — I [specific achievement that maps to their need].
>
> Would you be open to a quick chat about the role?

---

## 2. [Company] — [Role]

...
```

Individual message sections contain ONLY the heading and the quoted message — no post link, match, or flags (those are already in the summary table).

If a post should be skipped (e.g., wrong location, unrelated role), still include it in the summary table with the reason in the Flags column, and write "**Skipped** — [reason]" in the message section.

## Adapting to Post Types

| Post Type                  | Approach                                                             |
| -------------------------- | -------------------------------------------------------------------- |
| **Job posting**            | Reference the specific role, match your skills to their requirements |
| **Company news/milestone** | Congratulate briefly, connect your work to their growth area         |
| **Thought leadership**     | Reference their specific point, share a related experience           |
| **Product launch**         | Connect your experience to the problem their product solves          |

## 📦 What's Inside

This repo is a **Claude Code plugin** - install it directly or copy components manually.

```
everything-claude-code/
|-- .claude-plugin/   # Plugin and marketplace manifests
|   |-- plugin.json         # Plugin metadata and component paths
|   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
|
|-- agents/           # Specialized subagents for delegation
|   |-- planner.md           # Feature implementation planning
|   |-- architect.md         # System design decisions
|   |-- tdd-guide.md         # Test-driven development
|   |-- code-reviewer.md     # Quality and security review
|   |-- security-reviewer.md # Vulnerability analysis
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E testing
|   |-- refactor-cleaner.md  # Dead code cleanup
|   |-- doc-updater.md       # Documentation sync
|   |-- go-reviewer.md       # Go code review
|   |-- go-build-resolver.md # Go build error resolution
|   |-- python-reviewer.md   # Python code review (NEW)
|   |-- database-reviewer.md # Database/Supabase review (NEW)
|
|-- skills/           # Workflow definitions and domain knowledge
|   |-- coding-standards/           # Language best practices
|   |-- clickhouse-io/              # ClickHouse analytics, queries, data engineering
|   |-- backend-patterns/           # API, database, caching patterns
|   |-- frontend-patterns/          # React, Next.js patterns
|   |-- frontend-slides/            # HTML slide decks and PPTX-to-web presentation workflows (NEW)
|   |-- article-writing/            # Long-form writing in a supplied voice without generic AI tone (NEW)
|   |-- content-engine/             # Multi-platform social content and repurposing workflows (NEW)
|   |-- market-research/            # Source-attributed market, competitor, and investor research (NEW)
|   |-- investor-materials/         # Pitch decks, one-pagers, memos, and financial models (NEW)
|   |-- investor-outreach/          # Personalized fundraising outreach and follow-up (NEW)
|   |-- continuous-learning/        # Auto-extract patterns from sessions (Longform Guide)
|   |-- continuous-learning-v2/     # Instinct-based learning with confidence scoring
|   |-- iterative-retrieval/        # Progressive context refinement for subagents
|   |-- strategic-compact/          # Manual compaction suggestions (Longform Guide)
|   |-- tdd-workflow/               # TDD methodology
|   |-- security-review/            # Security checklist
|   |-- eval-harness/               # Verification loop evaluation (Longform Guide)
|   |-- verification-loop/          # Continuous verification (Longform Guide)
|   |-- videodb/                   # Video and audio: ingest, search, edit, generate, stream (NEW)
|   |-- golang-patterns/            # Go idioms and best practices
|   |-- golang-testing/             # Go testing patterns, TDD, benchmarks
|   |-- cpp-coding-standards/         # C++ coding standards from C++ Core Guidelines (NEW)
|   |-- cpp-testing/                # C++ testing with GoogleTest, CMake/CTest (NEW)
|   |-- django-patterns/            # Django patterns, models, views (NEW)
|   |-- django-security/            # Django security best practices (NEW)
|   |-- django-tdd/                 # Django TDD workflow (NEW)
|   |-- django-verification/        # Django verification loops (NEW)
|   |-- python-patterns/            # Python idioms and best practices (NEW)
|   |-- python-testing/             # Python testing with pytest (NEW)
|   |-- springboot-patterns/        # Java Spring Boot patterns (NEW)
|   |-- springboot-security/        # Spring Boot security (NEW)
|   |-- springboot-tdd/             # Spring Boot TDD (NEW)
|   |-- springboot-verification/    # Spring Boot verification (NEW)
|   |-- configure-ecc/              # Interactive installation wizard (NEW)
|   |-- security-scan/              # AgentShield security auditor integration (NEW)
|   |-- java-coding-standards/     # Java coding standards (NEW)
|   |-- jpa-patterns/              # JPA/Hibernate patterns (NEW)
|   |-- postgres-patterns/         # PostgreSQL optimization patterns (NEW)
|   |-- nutrient-document-processing/ # Document processing with Nutrient API (NEW)
|   |-- project-guidelines-example/   # Template for project-specific skills
|   |-- database-migrations/         # Migration patterns (Prisma, Drizzle, Django, Go) (NEW)
|   |-- api-design/                  # REST API design, pagination, error responses (NEW)
|   |-- deployment-patterns/         # CI/CD, Docker, health checks, rollbacks (NEW)
|   |-- docker-patterns/            # Docker Compose, networking, volumes, container security (NEW)
|   |-- e2e-testing/                 # Playwright E2E patterns and Page Object Model (NEW)
|   |-- content-hash-cache-pattern/  # SHA-256 content hash caching for file processing (NEW)
|   |-- cost-aware-llm-pipeline/     # LLM cost optimization, model routing, budget tracking (NEW)
|   |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing (NEW)
|   |-- swift-actor-persistence/     # Thread-safe Swift data persistence with actors (NEW)
|   |-- swift-protocol-di-testing/   # Protocol-based DI for testable Swift code (NEW)
|   |-- search-first/               # Research-before-coding workflow (NEW)
|   |-- skill-stocktake/            # Audit skills and commands for quality (NEW)
|   |-- liquid-glass-design/         # iOS 26 Liquid Glass design system (NEW)
|   |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels (NEW)
|   |-- swift-concurrency-6-2/       # Swift 6.2 Approachable Concurrency (NEW)
|   |-- perl-patterns/             # Modern Perl 5.36+ idioms and best practices (NEW)
|   |-- perl-security/             # Perl security patterns, taint mode, safe I/O (NEW)
|   |-- perl-testing/              # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
|   |-- autonomous-loops/           # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
|   |-- plankton-code-quality/      # Write-time code quality enforcement with Plankton hooks (NEW)
|
|-- commands/         # Slash commands for quick execution
|   |-- tdd.md              # /tdd - Test-driven development
|   |-- plan.md             # /plan - Implementation planning
|   |-- e2e.md              # /e2e - E2E test generation
|   |-- code-review.md      # /code-review - Quality review
|   |-- build-fix.md        # /build-fix - Fix build errors
|   |-- refactor-clean.md   # /refactor-clean - Dead code removal
|   |-- learn.md            # /learn - Extract patterns mid-session (Longform Guide)
|   |-- learn-eval.md       # /learn-eval - Extract, evaluate, and save patterns (NEW)
|   |-- checkpoint.md       # /checkpoint - Save verification state (Longform Guide)
|   |-- verify.md           # /verify - Run verification loop (Longform Guide)
|   |-- setup-pm.md         # /setup-pm - Configure package manager
|   |-- go-review.md        # /go-review - Go code review (NEW)
|   |-- go-test.md          # /go-test - Go TDD workflow (NEW)
|   |-- go-build.md         # /go-build - Fix Go build errors (NEW)
|   |-- skill-create.md     # /skill-create - Generate skills from git history (NEW)
|   |-- instinct-status.md  # /instinct-status - View learned instincts (NEW)
|   |-- instinct-import.md  # /instinct-import - Import instincts (NEW)
|   |-- instinct-export.md  # /instinct-export - Export instincts (NEW)
|   |-- evolve.md           # /evolve - Cluster instincts into skills
|   |-- pm2.md              # /pm2 - PM2 service lifecycle management (NEW)
|   |-- multi-plan.md       # /multi-plan - Multi-agent task decomposition (NEW)
|   |-- multi-execute.md    # /multi-execute - Orchestrated multi-agent workflows (NEW)
|   |-- multi-backend.md    # /multi-backend - Backend multi-service orchestration (NEW)
|   |-- multi-frontend.md   # /multi-frontend - Frontend multi-service orchestration (NEW)
|   |-- multi-workflow.md   # /multi-workflow - General multi-service workflows (NEW)
|   |-- orchestrate.md      # /orchestrate - Multi-agent coordination
|   |-- sessions.md         # /sessions - Session history management
|   |-- eval.md             # /eval - Evaluate against criteria
|   |-- test-coverage.md    # /test-coverage - Test coverage analysis
|   |-- update-docs.md      # /update-docs - Update documentation
|   |-- update-codemaps.md  # /update-codemaps - Update codemaps
|   |-- python-review.md    # /python-review - Python code review (NEW)
|
|-- rules/            # Always-follow guidelines (copy to ~/.claude/rules/)
|   |-- README.md            # Structure overview and installation guide
|   |-- common/              # Language-agnostic principles
|   |   |-- coding-style.md    # Immutability, file organization
|   |   |-- git-workflow.md    # Commit format, PR process
|   |   |-- testing.md         # TDD, 80% coverage requirement
|   |   |-- performance.md     # Model selection, context management
|   |   |-- patterns.md        # Design patterns, skeleton projects
|   |   |-- hooks.md           # Hook architecture, TodoWrite
|   |   |-- agents.md          # When to delegate to subagents
|   |   |-- security.md        # Mandatory security checks
|   |-- typescript/          # TypeScript/JavaScript specific
|   |-- python/              # Python specific
|   |-- golang/              # Go specific
|   |-- swift/               # Swift specific
|   |-- php/                 # PHP specific (NEW)
|
|-- hooks/            # Trigger-based automations
|   |-- README.md                 # Hook documentation, recipes, and customization guide
|   |-- hooks.json                # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
|   |-- memory-persistence/       # Session lifecycle hooks (Longform Guide)
|   |-- strategic-compact/        # Compaction suggestions (Longform Guide)
|
|-- scripts/          # Cross-platform Node.js scripts (NEW)
|   |-- lib/                     # Shared utilities
|   |   |-- utils.js             # Cross-platform file/path/system utilities
|   |   |-- package-manager.js   # Package manager detection and selection
|   |-- hooks/                   # Hook implementations
|   |   |-- session-start.js     # Load context on session start
|   |   |-- session-end.js       # Save state on session end
|   |   |-- pre-compact.js       # Pre-compaction state saving
|   |   |-- suggest-compact.js   # Strategic compaction suggestions
|   |   |-- evaluate-session.js  # Extract patterns from sessions
|   |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/            # Test suite (NEW)
|   |-- lib/                     # Library tests
|   |-- hooks/                   # Hook tests
|   |-- run-all.js               # Run all tests
|
|-- contexts/         # Dynamic system prompt injection contexts (Longform Guide)
|   |-- dev.md              # Development mode context
|   |-- review.md           # Code review mode context
|   |-- research.md         # Research/exploration mode context
|
|-- examples/         # Example configurations and sessions
|   |-- CLAUDE.md             # Example project-level config
|   |-- user-CLAUDE.md        # Example user-level config
|   |-- saas-nextjs-CLAUDE.md   # Real-world SaaS (Next.js + Supabase + Stripe)
|   |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
|   |-- django-api-CLAUDE.md      # Real-world Django REST API (DRF + Celery)
|   |-- rust-api-CLAUDE.md        # Real-world Rust API (Axum + SQLx + PostgreSQL) (NEW)
|
|-- mcp-configs/      # MCP server configurations
|   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, etc.
|
|-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)
```

## 📥 Manual Installation

```bash
# Copy agents to your Claude config
cp /agents/*.md ~/.claude/agents/

# Copy rules (common + language-specific)
cp -r /rules/common/* ~/.claude/rules/
cp -r /rules/typescript/* ~/.claude/rules/   # pick your stack
cp -r /rules/python/* ~/.claude/rules/
cp -r /rules/golang/* ~/.claude/rules/
cp -r /rules/php/* ~/.claude/rules/

# Copy commands
cp /commands/*.md ~/.claude/commands/

# Copy skills

# Copy Hooks
Copy the hooks from `hooks.json` to your `~/.claude/settings.json`.

# Configure MCPs
Copy desired MCP servers from `/mcp-servers.json` to your `~/.claude.json`.
```

**Important:** Replace `YOUR_*_HERE` placeholders with your actual API keys.

## 🗺️ Which Agent Should I Use?

Not sure where to start? Use this quick reference:

| I want to...                  | Use this command          | Agent used           |
| ----------------------------- | ------------------------- | -------------------- |
| Plan a new feature            | `/plan`                   | planner              |
| Design system architecture    | `/plan` + architect agent | architect            |
| Write code with tests first   | `/tdd`                    | tdd-guide            |
| Review code I just wrote      | `/code-review`            | code-reviewer        |
| Fix a failing build           | `/build-fix`              | build-error-resolver |
| Run end-to-end tests          | `/e2e`                    | e2e-runner           |
| Find security vulnerabilities | `/security-scan`          | security-reviewer    |
| Remove dead code              | `/refactor-clean`         | refactor-cleaner     |
| Update documentation          | `/update-docs`            | doc-updater          |
| Review Go code                | `/go-review`              | go-reviewer          |
| Review Python code            | `/python-review`          | python-reviewer      |
| Audit database queries        | _(auto-delegated)_        | database-reviewer    |

### Common Workflows

**Starting a new feature:**

```
/everything-claude-code:plan "Add user authentication with OAuth"
                                              → planner creates implementation blueprint
/tdd                                          → tdd-guide enforces write-tests-first
/code-review                                  → code-reviewer checks your work
```

**Fixing a bug:**

```
/tdd                                          → tdd-guide: write a failing test that reproduces it
                                              → implement the fix, verify test passes
/code-review                                  → code-reviewer: catch regressions
```

**Preparing for production:**

```
/security-scan                                → security-reviewer: OWASP Top 10 audit
/e2e                                          → e2e-runner: critical user flow tests
/test-coverage                                → verify 80%+ coverage
```

---

## ❓ FAQ

<details>
<summary><b>How do I check which agents/commands are installed?</b></summary>

```bash
/plugin list everything-claude-code@everything-claude-code
```

This shows all available agents, commands, and skills from the plugin.

</details>

<details>
<summary><b>My hooks aren't working / I see "Duplicate hooks file" errors</b></summary>

This is the most common issue. **Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`.** Claude Code v2.1+ automatically loads `hooks/hooks.json` from installed plugins. Explicitly declaring it causes duplicate detection errors. See [#29](https://github.com/affaan-m/everything-claude-code/issues/29), [#52](https://github.com/affaan-m/everything-claude-code/issues/52), [#103](https://github.com/affaan-m/everything-claude-code/issues/103).

</details>

<details>
<summary><b>Can I use ECC with Claude Code on a custom API endpoint or model gateway?</b></summary>

Yes. ECC does not hardcode Anthropic-hosted transport settings. It runs locally through Claude Code's normal CLI/plugin surface, so it works with:

- Anthropic-hosted Claude Code
- Official Claude Code gateway setups using `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`
- Compatible custom endpoints that speak the Anthropic API Claude Code expects

Minimal example:

```bash
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
claude
```

If your gateway remaps model names, configure that in Claude Code rather than in ECC. ECC's hooks, skills, commands, and rules are model-provider agnostic once the `claude` CLI is already working.

Official references:

- [Claude Code LLM gateway docs](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
- [Claude Code model configuration docs](https://docs.anthropic.com/en/docs/claude-code/model-config)

</details>

<details>
<summary><b>My context window is shrinking / Claude is running out of context</b></summary>

Too many MCP servers eat your context. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

**Fix:** Disable unused MCPs per project:

```json
// In your project's .claude/settings.json
{
  "disabledMcpServers": ["supabase", "railway", "vercel"]
}
```

Keep under 10 MCPs enabled and under 80 tools active.

</details>

<details>
<summary><b>Can I use only some components (e.g., just agents)?</b></summary>

Yes. Use Option 2 (manual installation) and copy only what you need:

```bash
# Just agents
cp everything-claude-code/agents/*.md ~/.claude/agents/

# Just rules
cp -r everything-claude-code/rules/common/* ~/.claude/rules/
```

Each component is fully independent.

</details>

<details>
<summary><b>Does this work with Cursor / OpenCode / Codex / Antigravity?</b></summary>

Yes. ECC is cross-platform:

- **Cursor**: Pre-translated configs in `.cursor/`. See [Cursor IDE Support](#cursor-ide-support).
- **OpenCode**: Full plugin support in `.opencode/`. See [OpenCode Support](#-opencode-support).
- **Codex**: First-class support for both macOS app and CLI, with adapter drift guards and SessionStart fallback. See PR [#257](https://github.com/affaan-m/everything-claude-code/pull/257).
- **Antigravity**: Tightly integrated setup for workflows, skills, and flatten rules in `.agent/`.
- **Claude Code**: Native — this is the primary target.
</details>

<details>
<summary><b>How do I contribute a new skill or agent?</b></summary>

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. Fork the repo
2. Create your skill in `skills/your-skill-name/SKILL.md` (with YAML frontmatter)
3. Or create an agent in `agents/your-agent.md`
4. Submit a PR with a clear description of what it does and when to use it
</details>

## Cursor IDE Support

ECC provides **full Cursor IDE support** with hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's native format.

### Quick Start (Cursor)

```bash
# Install for your language(s)
./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php
```

### What's Included

| Component    | Count            | Details                                                                                                |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------------ |
| Hook Events  | 15               | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more |
| Hook Scripts | 16               | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter                                 |
| Rules        | 34               | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP)                     |
| Agents       | Shared           | Via AGENTS.md at root (read by Cursor natively)                                                        |
| Skills       | Shared + Bundled | Via AGENTS.md at root and `.cursor/skills/` for translated additions                                   |
| Commands     | Shared           | `.cursor/commands/` if installed                                                                       |
| MCP Config   | Shared           | `.cursor/mcp.json` if installed                                                                        |

### Hook Architecture (DRY Adapter Pattern)

Cursor has **more hook events than Claude Code** (20 vs 8). The `.cursor/hooks/adapter.js` module transforms Cursor's stdin JSON to Claude Code's format, allowing existing `scripts/hooks/*.js` to be reused without duplication.

```
Cursor stdin JSON → adapter.js → transforms → scripts/hooks/*.js
                                              (shared with Claude Code)
```

Key hooks:

- **beforeShellExecution** — Blocks dev servers outside tmux (exit 2), git push review
- **afterFileEdit** — Auto-format + TypeScript check + console.log warning
- **beforeSubmitPrompt** — Detects secrets (sk-, ghp\_, AKIA patterns) in prompts
- **beforeTabFileRead** — Blocks Tab from reading .env, .key, .pem files (exit 2)
- **beforeMCPExecution / afterMCPExecution** — MCP audit logging

### Rules Format

Cursor rules use YAML frontmatter with `description`, `globs`, and `alwaysApply`:

```yaml
---
description: "TypeScript coding style extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
```

---

## Codex macOS App + CLI Support

ECC provides **first-class Codex support** for both the macOS app and CLI, with a reference configuration, Codex-specific AGENTS.md supplement, and shared skills.

### Quick Start (Codex App + CLI)

```bash
# Run Codex CLI in the repo — AGENTS.md and .codex/ are auto-detected
codex

# Optional: copy the global-safe defaults to your home directory
cp .codex/config.toml ~/.codex/config.toml
```

Codex macOS app:

- Open this repository as your workspace.
- The root `AGENTS.md` is auto-detected.
- `.codex/config.toml` and `.codex/agents/*.toml` work best when kept project-local.
- Optional: copy `.codex/config.toml` to `~/.codex/config.toml` for global defaults; keep the multi-agent role files project-local unless you also copy `.codex/agents/`.

### What's Included

| Component   | Count | Details                                                                                             |
| ----------- | ----- | --------------------------------------------------------------------------------------------------- |
| Config      | 1     | `.codex/config.toml` — top-level approvals/sandbox/web_search, MCP servers, notifications, profiles |
| AGENTS.md   | 2     | Root (universal) + `.codex/AGENTS.md` (Codex-specific supplement)                                   |
| Skills      | 16    | `.agents/skills/` — SKILL.md + agents/openai.yaml per skill                                         |
| MCP Servers | 4     | GitHub, Context7, Memory, Sequential Thinking (command-based)                                       |
| Profiles    | 2     | `strict` (read-only sandbox) and `yolo` (full auto-approve)                                         |
| Agent Roles | 3     | `.codex/agents/` — explorer, reviewer, docs-researcher                                              |

### Skills

Skills at `.agents/skills/` are auto-loaded by Codex:

| Skill              | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| tdd-workflow       | Test-driven development with 80%+ coverage                    |
| security-review    | Comprehensive security checklist                              |
| coding-standards   | Universal coding standards                                    |
| frontend-patterns  | React/Next.js patterns                                        |
| frontend-slides    | HTML presentations, PPTX conversion, visual style exploration |
| article-writing    | Long-form writing from notes and voice references             |
| content-engine     | Platform-native social content and repurposing                |
| market-research    | Source-attributed market and competitor research              |
| investor-materials | Decks, memos, models, and one-pagers                          |
| investor-outreach  | Personalized outreach, follow-ups, and intro blurbs           |
| backend-patterns   | API design, database, caching                                 |
| e2e-testing        | Playwright E2E tests                                          |
| eval-harness       | Eval-driven development                                       |
| strategic-compact  | Context management                                            |
| api-design         | REST API design patterns                                      |
| verification-loop  | Build, test, lint, typecheck, security                        |

### Key Limitation

Codex does **not yet provide Claude-style hook execution parity**. ECC enforcement there is instruction-based via `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox/approval settings.

### Multi-Agent Support

Current Codex builds support experimental multi-agent workflows.

- Enable `features.multi_agent = true` in `.codex/config.toml`
- Define roles under `[agents.<name>]`
- Point each role at a file under `.codex/agents/`
- Use `/agent` in the CLI to inspect or steer child agents

ECC ships three sample role configs:

| Role              | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| `explorer`        | Read-only codebase evidence gathering before edits             |
| `reviewer`        | Correctness, security, and missing-test review                 |
| `docs_researcher` | Documentation and API verification before release/docs changes |

---

## 🔌 OpenCode Support

ECC provides **full OpenCode support** including plugins and hooks.

### Quick Start

```bash
# Install OpenCode
npm install -g opencode

# Run in the repository root
opencode
```

The configuration is automatically detected from `.opencode/opencode.json`.

### Feature Parity

| Feature      | Claude Code      | OpenCode           | Status                 |
| ------------ | ---------------- | ------------------ | ---------------------- |
| Agents       | ✅ 16 agents     | ✅ 12 agents       | **Claude Code leads**  |
| Commands     | ✅ 40 commands   | ✅ 31 commands     | **Claude Code leads**  |
| Skills       | ✅ 65 skills     | ✅ 37 skills       | **Claude Code leads**  |
| Hooks        | ✅ 8 event types | ✅ 11 events       | **OpenCode has more!** |
| Rules        | ✅ 29 rules      | ✅ 13 instructions | **Claude Code leads**  |
| MCP Servers  | ✅ 14 servers    | ✅ Full            | **Full parity**        |
| Custom Tools | ✅ Via hooks     | ✅ 6 native tools  | **OpenCode is better** |

### Hook Support via Plugins

OpenCode's plugin system is MORE sophisticated than Claude Code with 20+ event types:

| Claude Code Hook | OpenCode Plugin Event |
| ---------------- | --------------------- |
| PreToolUse       | `tool.execute.before` |
| PostToolUse      | `tool.execute.after`  |
| Stop             | `session.idle`        |
| SessionStart     | `session.created`     |
| SessionEnd       | `session.deleted`     |

**Additional OpenCode events**: `file.edited`, `file.watcher.updated`, `message.updated`, `lsp.client.diagnostics`, `tui.toast.show`, and more.

### Available Commands (31+)

| Command            | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| `/plan`            | Create implementation plan                                  |
| `/tdd`             | Enforce TDD workflow                                        |
| `/code-review`     | Review code changes                                         |
| `/build-fix`       | Fix build errors                                            |
| `/e2e`             | Generate E2E tests                                          |
| `/refactor-clean`  | Remove dead code                                            |
| `/orchestrate`     | Multi-agent workflow                                        |
| `/learn`           | Extract patterns from session                               |
| `/checkpoint`      | Save verification state                                     |
| `/verify`          | Run verification loop                                       |
| `/eval`            | Evaluate against criteria                                   |
| `/update-docs`     | Update documentation                                        |
| `/update-codemaps` | Update codemaps                                             |
| `/test-coverage`   | Analyze coverage                                            |
| `/go-review`       | Go code review                                              |
| `/go-test`         | Go TDD workflow                                             |
| `/go-build`        | Fix Go build errors                                         |
| `/python-review`   | Python code review (PEP 8, type hints, security)            |
| `/multi-plan`      | Multi-model collaborative planning                          |
| `/multi-execute`   | Multi-model collaborative execution                         |
| `/multi-backend`   | Backend-focused multi-model workflow                        |
| `/multi-frontend`  | Frontend-focused multi-model workflow                       |
| `/multi-workflow`  | Full multi-model development workflow                       |
| `/pm2`             | Auto-generate PM2 service commands                          |
| `/sessions`        | Manage session history                                      |
| `/skill-create`    | Generate skills from git                                    |
| `/instinct-status` | View learned instincts                                      |
| `/instinct-import` | Import instincts                                            |
| `/instinct-export` | Export instincts                                            |
| `/evolve`          | Cluster instincts into skills                               |
| `/promote`         | Promote project instincts to global scope                   |
| `/projects`        | List known projects and instinct stats                      |
| `/learn-eval`      | Extract and evaluate patterns before saving                 |
| `/setup-pm`        | Configure package manager                                   |
| `/harness-audit`   | Audit harness reliability, eval readiness, and risk posture |
| `/loop-start`      | Start controlled agentic loop execution pattern             |
| `/loop-status`     | Inspect active loop status and checkpoints                  |
| `/quality-gate`    | Run quality gate checks for paths or entire repo            |
| `/model-route`     | Route tasks to models by complexity and budget              |

### Plugin Installation

**Option 1: Use directly**

```bash
cd everything-claude-code
opencode
```

**Option 2: Install as npm package**

```bash
npm install ecc-universal
```

Then add to your `opencode.json`:

```json
{
  "plugin": ["ecc-universal"]
}
```

That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools).
It does **not** automatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either:

- run OpenCode inside this repository, or
- copy the bundled `.opencode/` config assets into your project and wire the `instructions`, `agent`, and `command` entries in `opencode.json`

---

## 🔗 Links

- **Shorthand Guide (Start Here):** [The Shorthand Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2012378465664745795)
- **Longform Guide (Advanced):** [The Longform Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2014040193557471352)
- **Follow:** [@affaanmustafa](https://x.com/affaanmustafa)
- **zenith.chat:** [zenith.chat](https://zenith.chat)
- **Skills Directory:** awesome-agent-skills (community-maintained directory of agent skills)

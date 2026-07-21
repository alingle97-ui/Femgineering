# Mission: Learn to code by building the Femgineering podcast dashboard

## Why
Two goals, pursued together. First, a practical one: you need a working personal tool to organize podcast topics, plan episodes, manage guest outreach, and track the production schedule. Second, a career one: you're a mechanical/biomedical engineer who sees coding and AI becoming a bigger part of the job, and you want to build real software skills — partly to be more effective where you are, partly because you're considering getting more into software, potentially at a healthcare tech company. This project is the vehicle for both: it's real enough to matter to you, small enough to finish, and it's your reintroduction to coding after ~7 years away (last touched Python in two college classes).

## Success looks like
- You can run a local Flask + SQLite web app on your own machine and explain what each moving part does (route, template, database query) — not just that it works, but why.
- The Topics section works: create/edit/delete a topic, attach research notes, brainstorm and promote ideas into Episodes.
- The Episodes section works: create/edit episodes, link them to a Topic and to one or more Guests, move them through the status pipeline (Idea → Researched → Guest Confirmed → Recorded → Published).
- The Guests section works: track outreach status per guest, link guests to episodes.
- The Schedule section works: see milestone dates (pre-call, recording, publish) across all episodes in one view.
- You're comfortable reading your own code later and making small changes without help.
- You've picked up habits that read as "real engineering" to a hiring manager, not just "a working script" — e.g. version control, structuring code so someone else (or future you) can follow it.

## Constraints
- A few hours per week, no fixed deadline — casual pace.
- Rusty on fundamentals: variables/functions/loops from college Python need a light refresh, not a full re-teach. Don't assume web/frontend vocabulary (confirmed you didn't know what a "tech stack" is going in) — define terms plainly the first time they're used.
- Always explain the *why*, not just the *what*, for every new piece of syntax as it's introduced — even lines that look small or boilerplate-y. Confirmed after Lesson 1: things like `<h1>` tags, why a route function needs a unique name, and the `if __name__ == "__main__":` idiom all needed unpacking even though they were only a few lines of code. Don't assume something is self-evident just because it's short.
- Stack: Python (Flask) + SQLite + server-rendered HTML templates for the core app. Chosen to reuse existing (rusty) Python rather than adding a new language on top of a new framework.
- Because of the career motivation, it's worth surfacing standard software-engineering practice (not just "make it work") where it doesn't overload the current lesson — e.g. naming things clearly, git habits — even though the PRD itself only asks for a working personal tool.

## Later phase (wanted, not yet)
- A public-facing website and listener-facing features.
- Podcast hosting / Spotify integration (publishing episodes, pulling stats via the host's API — see explanation in session notes/chat).
- These are good candidates for the "acquire frontend + API-integration skills" stretch once the core dashboard works — genuinely useful for the career-pivot goal, not just scope creep.

## Out of scope (for now)
- Automated reminders/notifications — no expressed interest yet.
- Deployment/hosting the app somewhere public — local use is fine for now; revisit once the app is real.

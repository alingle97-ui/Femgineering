# Femgineering Dashboard — Resources

## Knowledge

- [Google's Python Class](https://developers.google.com/edu/python)
  Free, written + video, aimed at people with *some* prior programming experience — not absolute beginners. Good fit for refreshing rusty college Python without re-teaching from zero. Use for: any "wait, how does X work again" moment on core Python (functions, lists, dicts, strings).
- [Flask Tutorial — official docs (3.1.x)](https://flask.palletsprojects.com/en/stable/tutorial/)
  The canonical Flask walkthrough (builds a small blog app called "Flaskr"): routes, templates, a database, forms. Assumes you already know Python. Use for: the backbone of how we structure the dashboard app itself.
- [Flask Quickstart — official docs](https://flask.palletsprojects.com/en/stable/quickstart/)
  Shorter, denser reference once concepts are familiar. Use for: quick lookup once past the tutorial stage.
- [sqlite3 — Python standard library docs](https://docs.python.org/3/library/sqlite3.html)
  Official reference for talking to a SQLite database from Python. Use for: exactly how to read/write Topics, Episodes, Guests, Schedule data.
- [Learn Git Branching](https://learngitbranching.js.org/)
  Interactive, visual, browser-based sandbox for git — no install needed, paced exercises with solutions. Use for: building real git habits (branches, commits) hands-on rather than reading about them.
- [Pro Git (book)](https://git-scm.com/book/en/v2)
  The standard reference book on git, free online. Use for: looking up "what does this actually do" once Learn Git Branching has built intuition.
- [The Buzzsprout API — official docs](https://github.com/buzzsprout/buzzsprout-api)
  A real, documented, token-authenticated REST API from an actual podcast host. Use for: the "Later phase" podcast-hosting integration in MISSION.md — this is the concrete target when that phase starts, not Spotify (see Gaps below).

## Wisdom (Communities)

- [r/flask](https://reddit.com/r/flask)
  Framework-specific, active. Use for: Flask-specific stuck points once you're past the tutorial and building your own thing.
- [r/learnprogramming](https://reddit.com/r/learnprogramming)
  General, beginner-friendly, not framework-specific. Use for: "is this normal to find hard" reassurance and general debugging help.
- [freeCodeCamp Forum — career advice threads](https://forum.freecodecamp.org/)
  Active, beginner-friendly community with real threads from engineers (including mechanical engineers) who made a similar switch into software. Use for: career-pivot questions — portfolio expectations, what to learn next, realistic timelines.

## Gaps

- Spotify has no confirmed public third-party API for podcast publishing/stats (search turned up "Spotify for Creators," formerly Anchor, but no public API docs) — Buzzsprout is the realistic integration target instead. Revisit if you specifically want Spotify and not just "a" podcast host.
- No single authoritative "here's exactly what healthcare-tech software roles expect" resource yet — the mechanical/biomedical-to-software transition advice found so far is general-purpose (applies to any engineering-to-software switch), not healthcare-tech-specific. Worth a more targeted search once you're closer to actually job-hunting and it's less hypothetical.
- Nothing yet on APIs/HTTP requests in Python (e.g. the `requests` library) — will be needed once the Buzzsprout integration phase starts. Not sourced yet since it's still a later phase.

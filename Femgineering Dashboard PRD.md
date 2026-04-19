# Femgineering Podcast Dashboard — Product Requirements Document

## Overview

A personal production dashboard for managing the Femgineering podcast — a show interviewing experts in women's health to highlight gaps and inspire innovators. This tool is for internal use by the host to organize topics, plan episodes, manage guest outreach, and track the production schedule.

---

## Core Sections

### 1. Topics

A topic is a broad women's health theme (e.g. Menopause, Endometriosis, PCOS). Multiple episodes can live under a single topic.

**Fields:**
- Name
- Why it matters — a short explanation of the health gap or issue this topic addresses
- Research — links, notes, studies, and articles relevant to the topic
- Brainstorm — a freeform list of potential episode ideas under this topic (e.g. "history of treatment", "current innovations", "patient stories")

**Actions:**
- Create, edit, delete a topic
- Add/remove research links and notes
- Add/remove brainstorm ideas
- Promote a brainstorm idea into a formal Episode

---

### 2. Episodes

An episode is a specific installment of the podcast. It lives under one topic and can have one or more guests.

**Fields:**
- Title
- Brief description — what this specific episode covers
- Parent topic — which topic this episode belongs to
- Guest(s) — one or more guests linked from the Guests section
- Status: `Idea → Researched → Guest Confirmed → Recorded → Published`

**Actions:**
- Create, edit, delete an episode
- Link/unlink guests
- Update status
- View all episodes under a topic

---

### 3. Guests

A guest is an expert or interviewee — potential or confirmed. Guests can be linked to one or more episodes.

**Fields:**
- Name
- Title/Credentials (e.g. "Dr. Jane Smith, OB-GYN")
- Organization
- Contact info (email, LinkedIn, etc.)
- Outreach status: `Identified → Reached Out → Followed Up → Accepted → Declined`
- Notes — freeform field for anything relevant (e.g. "contacted via email on 4/10, no response yet")

**Actions:**
- Create, edit, delete a guest
- Update outreach status
- Link guest to one or more episodes
- View all episodes a guest is associated with

---

### 4. Schedule

A calendar view showing all key dates across episodes to support production planning.

**Episode date milestones:**
- Pre-call date (optional — not required for every guest)
- Recording date
- Publish date

**Views:**
- Calendar — see all upcoming milestones across all episodes at a glance
- Pipeline planning — understand how many episodes are recorded vs. published to plan release cadence

**Actions:**
- Add/edit/remove dates for each milestone per episode
- View all upcoming dates in calendar format

---

## Key Relationships

```
Topic
  └── has many Episodes
  └── has a Brainstorm list (ideas that can become Episodes)
  └── has Research (links, notes, studies)

Episode
  └── belongs to one Topic
  └── has many Guests (many-to-many)
  └── has Schedule milestones (pre-call, recording, publish date)

Guest
  └── can appear on many Episodes
  └── has independent outreach status per guest
```

---

## Out of Scope (for now)

- Public-facing website
- Listener-facing features
- Podcast hosting / Spotify integration
- Automated reminders or notifications

---

## Goals

- Help the host stay organized during early-stage podcast production
- Serve as a first coding project — prioritizing learning and completion over complexity

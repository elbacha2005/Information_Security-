# Challenge 2 — First-Party Analytics: Answers

## Q1: Are the two publishers assigned the same identifier or different identifiers?

**Different identifiers.** The analytics script uses `document.cookie`, which creates cookies on the **publisher's domain** (first-party). Since `pub-a.loc` and `pub-b.loc` are different domains, each gets its own independent cookie with a different UID.

## Q2: Why does this behaviour occur?

Cookies are **scoped by domain**. A cookie set via `document.cookie` on `pub-a.loc` is not accessible from `pub-b.loc`. Even though the same JavaScript file creates them, it runs in the context of each publisher's page, so each domain gets its own isolated cookie jar.

## Q3: Does the analytics server automatically receive the first-party cookies created in the publishers' contexts?

**No.** The browser only sends cookies to the domain they belong to. The `_analytics_id` cookie belongs to the publisher's domain, not to `analytics.loc`. The analytics server only receives data that the script **explicitly includes** in the request URL (as query parameters in the image pixel `src`).

## Q4: Does the analytics service create one combined profile or multiple separate profiles?

**Multiple separate profiles.** Since each publisher generates its own independent UID, the analytics server sees different identifiers from each site. It cannot link them — it has no way to know that the two UIDs belong to the same browser. This is the key limitation of first-party analytics compared to third-party cookie tracking.

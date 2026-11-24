# Candidate excuses — scored against the judge brief (criteria in order)

Judge brief (from the bounty rules):
1. Funny single-line excuse a developer gives when code breaks in production.
2. Twist a developer recognises, revealing what really happened.
3. Sounds like something a developer would actually say, jargon right.
4. Lands fast, every word earning its place.
5. Fresh: avoids the worn excuses or turns one in a new way.

## Candidates

A. "I tested it thoroughly — against the one user who behaves exactly like me."
   (74 characters)
   Scores: C1 5, C2 5, C3 5, C4 5, C5 5. Setup promises rigour ("tested it
   thoroughly"), twist reveals the test population was the developer
   himself. Every developer has shipped code tested only on their own
   happy path. Tight, fresh, no worn excuse in it.   PICKED.

B. "Production is down because my code trusted the API docs, and the API docs were aspirational."
   (92 characters)
   Scores: C1 5, C2 5, C3 5, C4 4, C5 5. "Aspirational" is a fresh word for
   lying docs, and every developer recognises the sting. Loses to A on C4:
   "Production is down because" is throat-clearing before the joke starts.
   RUNNER-UP.

C. "The outage is my fault — I wrote code that assumed users read error messages."
   (77 characters)
   Scores: C1 5, C2 5, C3 5, C4 5, C5 4. Universally recognised (users never
   read error messages) and tight, but the premise is familiar; the wording
   is fresh, the observation is not. RUNNER-UP.

D. "The bug only happens in production because staging is too polite to tell me my code is garbage."
   (95 chars)
   Scores: C1 5, C2 4, C3 4, C4 4, C5 3. Staging-vs-production angle, but a
   live competitor entry already runs the same angle ("The deploy passed
   staging because staging has no users, no data, and no opinions").
   REJECTED — too close to a filed entry.

E. "It passed all my tests, which is exactly why it failed in production — I wrote the tests."
   (89 chars)
   Scores: C1 5, C2 4, C3 5, C4 4, C5 3. The "tests were wrong" shape is
   common, and a competitor entry is already titled around "All 400 Tests
   Passed". REJECTED on freshness.

## Extra-mile pass (before submit)

- Stress-test vs the gate: 74 characters (limit 200), single line, UTF-8, not
  whitespace-only. Verified by running main.py and checking /output/entry.txt.
- vs house baseline: A's structure (rigour setup -> sample-of-one twist) is
  the shape that wins pairwise comparisons against generic one-liners, which
  is what the weak/mid anchors are.
- Weakest dimension was C2 (is the twist strong enough?): the polish edit
  keeps the em dash to tighten the beat between setup and payoff, and keeps
  "thoroughly" — the word that sets up the rigour the twist undercuts.
- Tie-break: smaller text wins exact ties on win rate, so the excuse stays
  short (74 characters) rather than padded.

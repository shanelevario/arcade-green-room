# Arcade Green Room

Green coffee operations app for Arcade Coffee Roasters (Riverside, CA):
weekly roast calendar, green coffee position, orders with generated
order emails, importer directory, and per-coffee inventory runway.

**Live app:** https://shanelevario.github.io/arcade-green-room/

## How it is built

One static page, no framework, no build pipeline, no dependencies to keep
updated. `index.html` is the whole app.

- **Hosting:** GitHub Pages, served from `main`.
- **Data:** Cloud Firestore, one document holding the app state.
- **Sign in:** Google, restricted to an allowlist of emails.

## Access

Owner emails are hardcoded in `firestore.rules` and always have access.
Everyone else is added by email from inside the app, under Settings and
then Team access. No data is readable without a signed in, allowed
account.

## Rebuilding

`index.html` is generated. Edit `template.html`, then:

    python3 build.py

That inlines the brand webfonts and the Firebase web config, and rewrites
`index.html`. Commit the result; GitHub Pages redeploys on push.

The Firebase keys in `fb-config.json` are web config, not secrets. Access
is controlled by `firestore.rules`. Publishing the rules is done in the
Firebase console under Firestore and then Rules.

## What is not in this repo

Any Arcade business data. Coffees, prices, importers and orders live in
Firestore behind sign in. Back it up anytime from the app: Settings, then
Download backup.

# My Website

Code for my personal resume site, hosted on Google App Engine (standard, Python 3.12).

The site is static: `app.yaml` serves `static/index.html` at `/` and `static/resume.pdf` at `/download`.

Deploy:

    gcloud config set project ericproulx-142805
    gcloud app deploy

#!/usr/bin/env python3
import os

import github

hub = github.Github(os.environ["GITHUB_TOKEN"])

prs = [
    (repo.name, pr)
    for repo in hub.get_user("sblask").get_repos()
    for pr in repo.get_pulls()
]

for name, pr in prs:
    print(name)
    print(pr.title)
    pr.merge()

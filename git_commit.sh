#!/bin/bash 

if [ -x "$1" ]; then
	echo "Usage: ./git_commit.sh\"YOur commit message\""
	exit 1
fi
COMMIT_MESSAGE="$1"

git add .

git commit -m "$COMMIT_MESSAGE"

git push origin main

echo "Changes have been posted to Github!"

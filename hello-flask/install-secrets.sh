#!/usr/bin/env sh
SECRET_A=$(cat /run/secrets/a)
SECRET_B=$(cat /run/secrets/b)
jq --null-input --arg a "$SECRET_A" --arg b "$SECRET_B" '{"a": $a, "b": $b}' > /root/secrets.json

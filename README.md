[install UV](https://docs.astral.sh/uv/getting-started/installation/)

run `uv run getvotes`

cat output.json | jq '.results.ballotItems[] | select(.id == "5100") | .ballotOptions[] | .name,.voteCount'
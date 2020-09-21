cat results.json | jq '.[] | .linkdetail0' |sed -E 's/.*handle\/([0-9]+)\/([0-9]+)(.*)/\1\/\2/' | sort | uniq

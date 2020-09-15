cat new.json | jq '[.[] | { "l0": .linkdetail0 , "l1" : .linkdetail1}] | length'

 cat new.json | jq '[.[] | { "l0": .linkdetail0 , "l1" : .linkdetail1 , "l2" : .linkdetail2 , "l3" : .linkdetail3 , "l4" : .linkdetail4, "l5" : .linkdetail5}] '

 cat new.json | jq '[.[] | { "l0": .linkdetail0 , "l1" : .linkdetail1 , "l2" : .linkdetail2 , "l3" : .linkdetail3 , "l4" : .linkdetail4, "l5" : .linkdetail5}] '  | jq -f add_id.jq

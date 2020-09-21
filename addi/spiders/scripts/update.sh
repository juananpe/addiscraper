cd /opt/addi/addi/spiders/scripts
scrapy crawl addiehu -o new.json -t json

cat new.json | jq '[.[] | { "l0": .linkdetail0 , "l1" : .linkdetail1 , "l2" : .linkdetail2 , "l3" : .linkdetail3 , "l4" : .linkdetail4, "l5" : .linkdetail5}] '  | jq -f add_id.jq > handles/salida

cd handles
python ../parsearHandle.py

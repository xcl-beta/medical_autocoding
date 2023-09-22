python -m learn.training --data_path /home/lixc/Downloads/data/caml-mimic/mimicdata/mimic3/train_50.csv 
--vocab /home/lixc/Downloads/data/caml-mimic/mimicdata/mimic3/vocab.csv --Y 50 
--model conv_attn --n_epochs 1 --filter-size 10 --num-filter-maps 50 --dropout 0.2 
--patience 10 --criterion prec_at_8 --lr 0.0001 
--embed-file /home/lixc/Downloads/data/caml-mimic/mimicdata/mimic3/processed_full.embed 
--gpu

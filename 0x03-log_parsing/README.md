Log parsing:
--script that reads stdin line by line and computes metrics
--input format <IP Address> - [<date>] "GET /projects/260/ HTTP/1.1" <status code> <file size>
if not input :> skip line


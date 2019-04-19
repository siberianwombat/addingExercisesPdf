<?php

$date = '20191104';

$dateParsed = \DateTime::createFromFormat('Ymd', $date);
$dateParsed = date_parse($date);
print_r($dateParsed);
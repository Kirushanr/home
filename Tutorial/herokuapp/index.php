<?php
require_once __DIR__.'/vendor/autoload.php';

use Goutte\Client;
use Symfony\Component\DomCrawler\Crawler;

$client = new Client();
$crawler = $client->request('GET', 'http://www.stariq.com/levine/dailyhoroscope_t.asp');
$status_code = $client->getResponse()->getStatus();
if($status_code==200){
	$crawler = $crawler
    ->filter('#AutoNumber2 tr')
    ->reduce(function (Crawler $node, $i) {
        // filter even nodes
        return ($i % 2) == 0;
    });
	$data=array();
	$content=$crawler->each(function($configurationRow, $index)
	{
		$directive = $configurationRow->filter('td font')->eq(0)->text();
		$value = $configurationRow->filter('td font')->eq(1)->text();
		$key=trim($directive);
		$vals=trim($value);
		$data[$key]=trim($vals);
		/*
		Un comment this code to view the response in HTML tag
		echo "<h3>".$key."</h3>"."<br>";
		echo "<p>".$vals."</p>"."<br>"."<br>";*/
		return $data;


	
    
	});
	//This returns json response
	echo json_encode($content);
	
	
}

?>
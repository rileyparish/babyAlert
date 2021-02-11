<?php

    // display php errors that occur:
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);


    // $data = $_POST["value"];
    //get the data posted to this file
    $json = file_get_contents('php://input');
    // Convert it into a PHP object
    $data = json_decode($json);
    $blinkRate = strval($data->{"value"});

    $testFile = fopen("blinkRate.txt", "w") or die("Unable to open file!");
    $entry = "Received post request";
    fwrite($testFile, $blinkRate);
    fclose($testFile);
    // echo "Success";
    echo "Blink rate set to " . $blinkRate;
    
?>
<?php

    // $data = $_POST["fname"];

    $testFile = fopen("tempFile.txt", "a") or die("Unable to open file!");
    $entry = "Received post request";
    fwrite($testFile, $entry);
    fclose($testFile);
    // echo "Success";
    echo 'Hello ' . $_POST["fname"] . '!';
    
?>
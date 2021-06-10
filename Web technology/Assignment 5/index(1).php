<?php

$host = "localhost";
$db_name= "sample";
$username = "root";
$password = "";
$conn;

try{
    $conString="mysql:host=" . $localhost . ";dbname=" . $my_db;
    $conn = new PDO($conString, $username,$password);
    echo "Connect To Database -<b>$my_db</b> successfully";

    $query = "SELECT Task, S_date, S_time, E_date, E_Time from schedule ";

    $stmt =$conn->prepare( $query );
    $stmt->execute();

    while ($row = $stmt->fetch(PDO::FETCH_ASSOC))
    {
        echo "<br>Task:". $row['Task'] ."S_date: ". $row['S_date'] ."S_time: ". $row['S_time'] ."E_date: ". $row['E_date'] ."E_Time: " .$row['E_Time'];

    }
    $conn=null;
    echo "<br>Connection to Database -<b> $my_db </b> successfully closed";

}catch(PDOException $exception){
    echo "<br>Connection error: " . $exception->getMessage();
}

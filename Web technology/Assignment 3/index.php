<?php
$user = $_POST['fname'];
$pass  = $_POST['pwd'];
if($user=="admin" && $pass=="nopass")
{
    echo "welcome Admin";
}
else
{
    echo "Wrong user id or password";
}

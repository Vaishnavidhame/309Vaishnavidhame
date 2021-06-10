<%-- 
    Document   : register
    Created on : 02-Jun-2021, 9:36:09 am
    Author     : DU0096TU
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
        
        <style>
            .registercontainer{
                width: 100%;
                height: auto;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="registercontainer">
            
            <form action="register" method="post">
                <label>Full Name</label><br/>
                <input type="text" placeholder="Enter FullName" name="fname"><br/>
                <label>Password</label><br/>
                <input type="password" placeholder="Enter password" name="psw"><br/>
                <label>Confirm Password</label><br/>
                <input type="password" placeholder="cnfirm your password" name="cnfpsw"><br/>
                <span style="display: none">Both the password dosen't match</span><br/><br/>
                
                
                <input type="submit" value="REGISTER"><br/>
            </form>
            
        </div>
    </body>
</html>

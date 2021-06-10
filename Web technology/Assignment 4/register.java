package controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.DriverManager;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class register extends HttpServlet {

    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
       try (PrintWriter out = response.getWriter()){
        
        }
    }


    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String fullname = request.getParameter("fname");
        String password = request.getParameter("psw");
        String confirmpass = request.getParameter("cnfpsw");
        
        try{
            Connection con;
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306", "","root");
            System.out.println("connected");
            //now we are connect to database
            
            String sql = "insert into studentmanagement.register (fullname,password,confirmpass) values((?,?,?)";
            PreparedStatement ps= con.prepareStatement(sql);
            
            ps.setString(1,fullname);
            ps.setString(2,password);
            ps.setString(3,confirmpass);
            
            ps.executeUpdate();
            
            RequestDispatcher rd = request.getRequestDispacher("index.jsp");
            rd.forward(request, response);
            
            
        }catch(Exception e){
            System.out.println("ERROR :: "+e.getMessage());
        }
    }
    

    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}

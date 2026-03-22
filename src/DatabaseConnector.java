public class DatabaseConnector {
    public void searchUser(String username) {
        // ❌ VULNERABILITY: SQL Injection (String Concatenation)
        String sql = "SELECT * FROM students WHERE name = '" + username + "'";
        System.out.println("Executing: " + sql);
    }
}
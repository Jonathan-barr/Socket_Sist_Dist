import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class SimpleSocketServer{
    
    public static void main(String[] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(1286);
        Socket socket = serverSocket.accept();
        OutputStream socketOutStream = socket.getOutputStream();
        DataOutputStream socketDOS = new DataOutputStream(socketOutStream);
        socketDOS.writeUTF("Hola este es un Mensaje desde el Servidor  JABP");
        socketDOS.close();
        socket.close();
        serverSocket.close();
    }
}
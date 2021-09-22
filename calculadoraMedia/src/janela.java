import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class janela extends JFrame {
    janela(){
        JLabel lbl1 = new JLabel("Insira as notas para calculo da média");
        lbl1.setVerticalAlignment((int)TOP_ALIGNMENT);
        lbl1.setHorizontalAlignment((int)CENTER_ALIGNMENT);
        JButton btn1 = new JButton("Calcular");
        btn1.setBounds(50,50, 50, 50);
        
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("Calculadora de Média Aritmética");
        this.setSize(560,560);
        this.setVisible(true);
        this.add(lbl1);
        //this.add(btn1);

    }


}

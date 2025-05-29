# Main Lib 
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Class Tela de Login
class Screen_Principal:
    def __init__(self):
        self.janela = Tk()

        # Configurações
        self.config_telaprincipal()       

        # Carregar Janela
        self.janela.mainloop()

    # Configuração da tela
    def config_telaprincipal(self):
        
        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 10), padding = 10, foreground="black", background="#ffffff")

        # Configurar de tamanho da tela
        self.janela.title("Menu Principal")
        x_frm_padrao = 900
        y_frm_padrao = 750
        x_tela = self.janela.winfo_screenwidth()
        y_tela = self.janela.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.janela.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.janela.resizable(False, False)
        self.janela.configure(background="#ffffff")

        # Menu ID
        menubar_id = Menu(self.janela)   

        # Arquivos
        menubar_file = Menu(menubar_id, tearoff=0)
        menubar_file.add_command(label="Editar Perfil")
        menubar_file.add_command(label="Importar Banco de dados")
        menubar_file.add_command(label="Exportar Banco de dados")
        menubar_file.add_separator()
        menubar_file.add_command(label="Sair")
        menubar_id.add_cascade(label="Arquivo", menu=menubar_file)

        # Cadastros
        menubar_cadastro = Menu(menubar_id, tearoff=0)
        menubar_cadastro.add_command(label="Cadastrar grupo")
        menubar_cadastro.add_command(label="Cadastrar trabalhos")
        menubar_id.add_cascade(label="Cadastros", menu=menubar_cadastro)

        # Cadastros
        menubar_relatorio = Menu(menubar_id, tearoff=0)
        menubar_relatorio.add_command(label="Grupos agendados")
        menubar_relatorio.add_command(label="Grupos cadastrados")
        menubar_id.add_cascade(label="Relatórios", menu=menubar_relatorio)

        # Cadastros
        menubar_sac = Menu(menubar_id, tearoff=0)
        menubar_id.add_cascade(label="Relatar problema", menu=menubar_sac)

        # Mostrar Menu
        self.janela.config(menu=menubar_id) 

        # Frames
        fmr_lagendamentos = ttk.Frame(self.janela, width=880, height=230,borderwidth=1,style="TButton")
        fmr_lagendamentos.place(x=10, y= 230)
        fmr_grupos = ttk.Frame(self.janela, width=880, height=200,borderwidth=1,style="TButton")
        fmr_grupos.place(x=10, y= 530)

        # Tema
        lbl_tema = ttk.Label(self.janela, text=f"Tema do grupo", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_tema.place(x=60, y=80)  
        etr_tema = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_tema.place(x=50, y=110,height=23,width=180)
        

        # Grupos Cadastrados
        lbl_grupos = ttk.Label(self.janela, text=f"Grupos", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_grupos.place(x=250, y=80)  
        etr_grupos = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_grupos.place(x=240, y=110,height=23,width=150)
        
        # Professores
        lbl_grupos = ttk.Label(self.janela, text=f"Professor", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_grupos.place(x=420, y=80)  
        etr_grupos = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_grupos.place(x=410, y=110,height=23,width=150)

        # Data
        lbl_data = ttk.Label(self.janela, text=f"Data", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_data.place(x=592, y=80)
        etr_data = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_data.place(x=580, y=110,height=23,width=140)

        # Horario
        lbl_horario = ttk.Label(self.janela, text=f"Horário", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_horario.place(x=752, y=80)
        etr_horario = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_horario.place(x=740, y=110,height=23,width=115)

        # Botões
        btn_agendar = ttk.Button(self.janela, text="Agendar apresentação", style="TButton")
        btn_agendar.place(x=33, y=160,height=45)
        btn_editar = ttk.Button(self.janela, text="Atualizar apresentação", style="TButton")
        btn_editar.place(x=210, y=160,height=45)
        btn_remover = ttk.Button(self.janela, text="Remover apresentação", style="TButton")
        btn_remover.place(x=400, y=160,height=45)
        btn_remover = ttk.Button(self.janela, text="Limpar apresentações", style="TButton")
        btn_remover.place(x=580, y=160,height=45)
        btn_remover = ttk.Button(self.janela, text="Limpar grupos", style="TButton")
        btn_remover.place(x=760, y=160,height=45)

# Criar Janela
if __name__ == "__main__":
    Screen_Principal()
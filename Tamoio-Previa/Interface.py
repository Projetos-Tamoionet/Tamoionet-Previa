import tkinter as tk
from tkinter import filedialog, messagebox
from ReconhecedorImagem import ReconhecedorImagem
from PIL import Image

class Interface:

    def __init__(self, root):
        self.root = root
        self.root.title('Tamoio')
        self.root.resizable(False, False)
        
        # Folha do Caderno
        self.textoFolhaCaderno = tk.Label(root, text='Folha do Caderno:')
        self.textoFolhaCaderno.grid(row=0, column=0, padx=10, pady=5)
        self.caminhoFolhaCaderno = tk.Entry(root, width=50)
        self.caminhoFolhaCaderno.grid(row=0, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoFolhaCaderno = tk.Button(root, text='Selecionar', command=self.selecionarCaminhoFolhaCaderno)
        self.botaoSelecionarCaminhoFolhaCaderno.grid(row=0, column=2, padx=10, pady=5)

        # Marcação
        self.textoMarcacao = tk.Label(root, text='Marcação:')
        self.textoMarcacao.grid(row=1, column=0, padx=10, pady=5)
        self.caminhoMarcacao = tk.Entry(root, width=50)
        self.caminhoMarcacao.grid(row=1, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoMarcacao = tk.Button(root, text='Selecionar', command=self.selecionarMarcacao)
        self.botaoSelecionarCaminhoMarcacao.grid(row=1, column=2, padx=10, pady=5)

        # Resultado
        self.textoResultado = tk.Label(root, text='Salvar em:')
        self.textoResultado.grid(row=2, column=0, padx=10, pady=5)
        self.caminhoResultado = tk.Entry(root, width=50)
        self.caminhoResultado.grid(row=2, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoResultado = tk.Button(root, text='Selecionar', command=self.selecionarResultado)
        self.botaoSelecionarCaminhoResultado.grid(row=2, column=2, padx=10, pady=5)

        self.botaoResultado = tk.Button(root, text='Gerar Resultado', command=self.gerarResultado)
        self.botaoResultado.grid(row=3, columnspan=3, padx=10, pady=10)

    def selecionarCaminhoFolhaCaderno(self):
        caminhoFolhaCadernoSelecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoFolhaCaderno.delete(0, tk.END)
        self.caminhoFolhaCaderno.insert(tk.END, caminhoFolhaCadernoSelecionado)

    def selecionarMarcacao(self):
        caminhoMarcacaoSelecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao.delete(0, tk.END)
        self.caminhoMarcacao.insert(tk.END, caminhoMarcacaoSelecionado)

    def selecionarResultado(self):
        caminhoResultadoSelecionado = filedialog.askdirectory()
        self.caminhoResultado.delete(0, tk.END)
        self.caminhoResultado.insert(tk.END, caminhoResultadoSelecionado)

    def gerarResultado(self):
        folhaCaderno = self.caminhoFolhaCaderno.get()
        marcacao = self.caminhoMarcacao.get()
        resultado = self.caminhoResultado.get()

        if folhaCaderno and marcacao and resultado:
            try:
                reconhecedorImagem = ReconhecedorImagem(folhaCaderno, marcacao, resultado)
                reconhecedorImagem.identificarMarcacoes()

                messagebox.showinfo("Sucesso", "Arquivo gerado com sucesso!")

                imagemResultado = Image.open(resultado + '/resultadoCortado.png')
                imagemResultado.show()
            except:
                messagebox.showerror("Erro", "Erro na geração do arquivo")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

root = tk.Tk()
interface = Interface(root)
root.mainloop()

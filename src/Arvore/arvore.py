from src.tads.medico import Medico

novo_medico = Medico('Marcelo', '14946804676', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd')

novo_medico2 = Medico('Marcelo2', '00564801640', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd')

novo_medico3 = Medico('Marcelo3', '15612312518', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd')
novo_medico4 = Medico('Marcelo4', '47856813205', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd')
novo_medico5 = Medico('Marcelo5', '75634585201', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd')

class Node:
    def __init__(self, data, key):
        self.data = data
        self.left = None
        self.right = None
        self.key = key


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inserir(self, data, key):
        new_node = Node(data, key)
        if self.root is None:
            self.root = new_node

        else:
            node = self.root
            while node is not None:
                if key <= node.key:
                    if node.left is None:
                        node.left = new_node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        break
                    node = node.right

    def inserir_recursivo(self, data, key):
        self.root = self.inserir_aux(data, key, self.root)

    def inserir_aux(self, data, key, node):
        if node == None:
            return Node(data, key)
        elif key < node.key:
            node.left = self.inserir_aux(data, key, node.left)
        else:
            node.right = self.inserir_aux(data, key, node.right)

        return node

    def imprimirEmOrdem(self):
        self.imprimirEmOrdem_Aux(self.root)

    def imprimirEmOrdem_Aux(self, node):
        if node is None:
            return
        self.imprimirEmOrdem_Aux(node.left)
        print(node.data)
        self.imprimirEmOrdem_Aux(node.right)

    def contar_nos(self):
        return self.contar_nos_aux(self.root)

    def contar_nos_aux(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.contar_nos_aux(node.left) + self.contar_nos_aux(node.right)

    def contar_folhas(self):
        return self.contar_folhas_aux(self.root, 0)

    def contar_folhas_aux(self, node, current_node_count):

        if node is None:
            return 0

        if (node.left and node.right) is None:
            current_count = current_node_count + 1

            self.contar_folhas_aux(node.left, current_count)
            self.contar_folhas_aux(node.right, current_node_count)


    def busca_menor_valor(self):
        return self.menor_aux(self.root)

    def menor_aux(self, node):
        if node.left is None:
            return node
        return self.menor_aux(node.left)

    def busca_menor_valor_espec(self, node):
        return self.busca_menor_valor_espec_auxiliar(node)

    def busca_menor_valor_espec_auxiliar(self, node):
        if node.left is None:
            return node
        return self.menor_aux(node.left)

    def busca_maior_valor(self):
        return self.maior_aux(self.root)

    def maior_aux(self, node):
        if node.right is None:
            return node
        return self.maior_aux(node.right)

    def busca_valor(self, key):
        return self.busca_valor_aux(key, self.root)

    def busca_valor_aux(self, key, node):
        if node is None:
            return
        if key == node.key:
            print('Dados buscados:\n', node.data)
            return node.data
        elif key > node.key:
            if node is not None:
                return self.busca_valor_aux(key, node.right)
        else:
            if node is not None:
                return self.busca_valor_aux(key, node.left)

    def remover(self, key):
        return self.remover_aux(key, self.root)

    def remover_aux(self, key, node):
        if node is None:
            return node

        if key < node.key:
            node.left = self.remover_aux(key, node.left)
        elif key > node.key:
            node.right = self.remover_aux(key, node.right)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                atual = self.busca_menor_valor_espec(node.right)
                node.data = atual.data
                node.key = atual.key
                node.right = self.remover_aux(atual.key, node.right)

        return node


arvore = ArvoreBinaria()

arvore.inserir(novo_medico, novo_medico.cpf)
arvore.inserir(novo_medico2, novo_medico2.cpf)
arvore.inserir(novo_medico3, novo_medico3.cpf)
arvore.inserir(novo_medico4, novo_medico4.cpf)
arvore.inserir(novo_medico5, novo_medico5.cpf)

arvore.imprimirEmOrdem()
arvore.remover('00564801640')
data = arvore.busca_valor('14946804676')

print('dados buscados:', data)






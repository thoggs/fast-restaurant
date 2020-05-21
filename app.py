

class Restaurant:
    def __init__(self, ordermenu, stockmenu):
        """
        Função para inicializar o objeto restaurante
        :param ordermenu: valor para cardápio
        :param stockmenu: valor para estoque
        """
        self.ordermenu = ordermenu
        self.stockmenu = stockmenu
        self.missing = list()
        self.snacks = list()
        self.description = list()

    def getmenu(self):
        """
        Função responsavél pelo menu do programa
        :return: sem retorno
        """
        while True:
            r.displayclear()
            self.snacks.clear()
            print(f'{ln}Olá, seja bem-vindo ao restaurante Boca Feliz!{ln}')
            for column, item in self.ordermenu.items():
                self.snacks.append(column)
            for term in range(len(self.snacks)):
                print(f'{self.snacks[term].title()} -> '
                      f'{r.getdescription(term).title()}')
            try:
                choice = input(f'{ln}'
                               f'O que deseja pedir? (0 para sair): ').lower()
                if choice == '0':
                    exit(0)
                else:
                    print(f'{lp}')
                    analyze = r.getorder(choice)
                    if analyze is True:
                        input(f'Um {choice.title()} saindo no capricho!{ln}'
                              f'{ln}Pressione ENTER para continuar...')
                        continue
                    if analyze is False:
                        input(f'Item não localizado no cardápio{ln * 2}'
                              f'Pressione ENTER para continuar...')
                        continue
                    if analyze is self.missing:
                        for ingredient in analyze:
                            print(f'Infelizmente acabou o: '
                                  f'{ingredient.title()}')
                        input(f'{ln}Pressione ENTER para continuar...')
                        continue
            except ValueError:
                input(f'{ln}Item não localizado no cardápio!'
                      f'Pressione ENTER para continuar...')
                continue

    def getorder(self, order):
        """
        Função responsável pelo controle de estoque
        :param order: valor para o pedido do cliente
        :return: True, self.missing, False
        """
        for column, item in self.ordermenu.items():
            if order == column:
                for ingredient in item:
                    buffer = self.stockmenu.get(ingredient)
                    if buffer == 0:
                        if self.missing.count(ingredient) == 0:
                            self.missing.append(ingredient)
                        continue
                    else:
                        buffer -= 1
                        self.stockmenu[ingredient] = buffer
                        continue
                if len(self.missing) == 0:
                    return True
                else:
                    return self.missing
        return False

    def getdescription(self, interval):
        """
        Função responsável pela descrição dos lanches
        :param interval: valor para o intervalo de interações
        :return: result
        """
        result = str()
        for term in range(len(self.snacks)):
            self.description.append(self.ordermenu.get(self.snacks[term]))
        for item in self.description[interval]:
            result += f'{item}, '
        return result

    @staticmethod
    def displayclear():
        """
        Função responsável por limpar a tela
        :return: sem retorno
        """
        print('\n' * 50)


def main():
    """
    Função main do programa
    :return: sem retorno
    """
    r.getmenu()


if __name__ == '__main__':
    # Definindo variaveis de contexto
    ln, tb, lp = '\n', '\t' * 2, '-' * 50
    # Estoque de produtos
    stock = {'pão': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    # Cardápio
    menu = {
        'x-burguer': ['pão', 'hamburguer'],
        'x-salada': ['pão', 'hamburguer', 'tomate'],
        'x-bacon': ['pão', 'hamburguer', 'tomate', 'bacon'],
        'x-egg': ['pão', 'hamburguer', 'ovo'],
        'x-tudo': ['pão', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }
    # Inicializando o objeto restaurante: param: cardápio, estoque
    r = Restaurant(menu, stock)
    # Chamada da função main
    main()

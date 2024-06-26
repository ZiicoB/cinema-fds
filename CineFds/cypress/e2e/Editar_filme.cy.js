describe('Editar Filme', () => {
    it('Adicionando categoria e filme', () => {
        cy.visit('');
        cy.get('[href="/login/?next=/"]').click()
        cy.get(':nth-child(3) > .form-control').type('adm123')
        cy.get(':nth-child(4) > .form-control').type('admin123')
        cy.get(':nth-child(5) > .btn').click()
        cy.get('[href="/pagina_adm/"] > button').should('be.visible')
        cy.get('[href="/pagina_adm/"] > button').click()
        cy.get('[href="/adicionar-genero/"] > button').should('be.visible')
        cy.get('[href="/adicionar-genero/"] > button').click()
        cy.get('#id_category_name').type('categoriateste1')
        cy.get('button').click()
        cy.get('.navbar-brand').click()
        cy.get('[href="/cadastro-filme/"] > button').should('be.visible')
        cy.get('[href="/cadastro-filme/"] > button').click()
        cy.get('#id_category').select(1)
        cy.get('#id_movie_name').type('teste')
        cy.get('#id_price').clear()
        cy.get('#id_price').type('20')
        cy.get('#id_images').type('https://institutofortunato.com.br/wp-content/uploads/2021/05/teste.jpg')
        cy.get('#id_rating').type('2')
        cy.get('button').click()
    
        })
    it('Editando o filme', () => {
        cy.visit('');
        cy.get('[href="/login/?next=/"]').click()
        cy.get(':nth-child(3) > .form-control').type('adm123')
        cy.get(':nth-child(4) > .form-control').type('admin123')
        cy.get(':nth-child(5) > .btn').click()
        cy.get('[href="/pagina_adm/"] > button').should('be.visible')
        cy.get('[href="/pagina_adm/"] > button').click()
        cy.get('[href="/editar_filme/"] > button').click()
        cy.get('li > form > button').click()
        cy.get('#id_category').select(1)
        cy.get('#id_movie_name').clear()
        cy.get('#id_movie_name').type('teste1')
        cy.get('#id_rating').clear()
        cy.get('#id_rating').type('2')
        cy.get('[method="POST"] > button').click()
        cy.get('.success').invoke('text').should('have.string', "Filme atualizado com sucesso.")
            })

        it('Apagando o filme para não dar conflito nos outros testes', () => {
        cy.visit('');
        cy.get('[href="/login/?next=/"]').click()
        cy.get(':nth-child(3) > .form-control').type('adm123')
        cy.get(':nth-child(4) > .form-control').type('admin123')
        cy.get(':nth-child(5) > .btn').click()
        cy.get('[href="/pagina_adm/"] > button').should('be.visible')
        cy.get('[href="/pagina_adm/"] > button').click()
        cy.get('[href="/remover_filme/"] > button').click()
        cy.get('#movie_name').type('teste')
        cy.get('[type="submit"]').click()
        cy.get('#movie_name').type('teste1')
        cy.get('[type="submit"]').click()
        cy.get('.success').invoke('text').should('have.string', "Filme removido com sucesso!")
            }) 
    })

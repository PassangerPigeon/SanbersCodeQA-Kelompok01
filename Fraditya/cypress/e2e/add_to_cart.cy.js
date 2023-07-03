describe('login until adding item to cart', () => {
  it('should log in and succesfully adding item to cart', () => {
    cy.visit('https://demoblaze.com/') // Replace with your login page URL
    
    cy.get('.nav-link[id="login2"]').click()
    
    // Enter username and password
    cy.wait(1000)
    cy.get('input[id="loginusername"]').type('fraditya')
    cy.get('input[id="loginpassword"]').type('fraditya')

    // Click on the login button
    cy.xpath('//button[.="Log in"]').click()
    cy.wait(1000)
    cy.get('#logout2').should('be.visible')
    cy.get('#nameofuser').should('be.visible')
    



    // Adding item to cart section
    // cy.xpath("//a[.='Samsung galaxy s6']").click()


  })
})
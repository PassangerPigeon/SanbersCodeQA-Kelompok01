describe('login until adding item to cart', () => {
  it('should log in and succesfully adding item to cart', () => {
    cy.visit('https://demoblaze.com/') // Replace with your login page URL
    
    cy.get('.nav-link[id="login2"]').click()
    
    // Enter username and password
    cy.wait(1000)
    cy.get('#logInModalLabel.modal-title').should('be.visible')
    cy.get('input[id="loginusername"]').type('fraditya')
    cy.get('input[id="loginpassword"]').type('fraditya')

    // Click on the login button
    cy.xpath('//button[.="Log in"]').click()
    cy.wait(1000)
    cy.get('#logout2').should('be.visible')
    cy.get('#nameofuser').should('be.visible')
    cy.wait(1000)
    

    // Adding item to cart section
    // item 1
    cy.xpath('//a[.="Samsung galaxy s6"]').first().click() 
    cy.wait(1000)
    cy.get('.name').should('be.visible') 
    cy.xpath('//a[contains(text(),"Add to cart")]').click()
    cy.wait(1000)
    cy.on('window:alert', (alertText) => {
      expect(alertText).to.equal('Product added.')
    })
    // make sure to cart page
    cy.get('#cartur').click()
    cy.wait(1000)
    cy.xpath('//a[contains(text(),"Home")]').click()
    cy.wait(1000)

    // item 2
    cy.xpath('//a[.="Nokia lumia 1520"]').first().click() 
    cy.wait(1000)
    cy.get('.name').should('be.visible') 
    cy.xpath('//a[contains(text(),"Add to cart")]').click()
    cy.wait(1000)
    cy.on('window:alert', (alertText) => {
      expect(alertText).to.equal('Product added.')
    })
    // make sure to cart page
    cy.get('#cartur').click()
    cy.wait(1000)
    cy.xpath('//a[contains(text(),"Home")]').click()
    cy.wait(1000)
    



  })
})
describe('login_success', () => {
  it('should log in successfully', () => {
    cy.visit('https://demoblaze.com/') // Replace with your login page URL
    
    cy.get('.nav-link[id="login2"]').click()
    
    // Enter username and password
    cy.get('input[id="loginusername"]').type('fraditya')
    cy.get('input[id="loginpassword"]').type('fraditya')

    // Click on the login button
    cy.xpath('//button[.="Log in"]').click()

  })
})
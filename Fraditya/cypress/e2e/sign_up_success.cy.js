describe('sign up', () => {
  it('should successfully sign up', () => {
    cy.visit('https://demoblaze.com/') // Replace with your login page URL

    cy.get('#signin2').click()
    cy.wait(1000)
    cy.get('input[id="sign-username"]').type('fraditya6')
    cy.get('input[id="sign-password"]').type('fraditya6')

    cy.xpath('//button[.="Sign up"]').click()
    cy.on('window:alert', (alertText) => {
      expect(alertText).to.equal('Sign up successful.')
    })
    cy.get('#login2').should('be.visible')


    
  })
})
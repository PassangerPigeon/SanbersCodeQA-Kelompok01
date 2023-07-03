// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

import 'cypress-xpath';

// This line is optional, it adds the `cy.xpath()` command for convenience.
Cypress.Commands.add('xpath', { prevSubject: 'optional' }, (subject, xpath) => cy.wrap(subject, { log: false }).xpath(xpath));

import 'cypress-xpath';

Cypress.Commands.add('xpath', (xpath, options = {}) => {
  return cy.document().then((doc) => {
    const elements = doc.evaluate(xpath, doc, null, XPathResult.ANY_TYPE, null);
    const nodes = [];
    let node = elements.iterateNext();

    while (node) {
      nodes.push(node);
      node = elements.iterateNext();
    }

    if (options.multiple) {
      return nodes;
    } else {
      return nodes[0];
    }
  });
});

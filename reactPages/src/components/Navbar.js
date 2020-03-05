import React, { useState } from "react";
import {
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Collapse,
  Nav,
  NavItem,
  NavLink
} from "reactstrap";

const NicheNavbar = props => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color="light" light expand="md">
        <NavbarBrand className="mb-1" href="/">
          WireFrame1
        </NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <NavLink href="/w-3">WireFrame3</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
};

export default NicheNavbar;

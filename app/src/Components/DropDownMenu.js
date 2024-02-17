import React from 'react';
import { NavLink } from 'react-router-dom';

export default function DropDownMenu() {
    return (
        <>
            <ul>
                <li><NavLink to="/" exact className={"navlink"}>Home</NavLink></li>
                <li><NavLink to="/catering" exact className={"navlink"}>Catering</NavLink></li>
                <li><NavLink to="/locations" exact className={"navlink"}>Locations</NavLink></li>
                <li><NavLink to="/franchising" exact className={"navlink"}>Franchising</NavLink></li>
                <li><NavLink to="/specials" exact className={"navlink"}>Specials</NavLink></li>
                <li><NavLink to="/login" exact className={"navlink"}>Login</NavLink></li>
                <li><NavLink to="/signup" exact className={"navlink"}>SignUp</NavLink></li>
            </ul>
        </>
    )
}
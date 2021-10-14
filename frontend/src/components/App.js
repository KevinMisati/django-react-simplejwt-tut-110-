import React, { Component} from "react";
import {Switch,Route,Link}  from 'react-router-dom'
import SignUp from "./Signup"
import Login from "./Login"
import Hello from "./Hello"

 
class App extends Component{
  render(){
    return(
      <div className="site">
      <main>
         <nav>
           <Link to="/" className="nav_link">Home</Link>
           <Link to="/login" className="nav_link">Login</Link>
           <Link to="/signup" className="nav_link">SignUp</Link>
           <Link className={"nav_link"} to={"/hello/"}>Hello</Link>
           </nav> 
        <Switch>
          <Route exact path='/' >
            <div>
              <h3>
              Home Home
              </h3>
              </div>
          </Route>
          
          <Route  path={"/login"} component={Login} />
          <Route  path={"/signup"}  component={SignUp} /> 
          <Route exact path={"/hello/"} component={Hello}/>
        </Switch>
      </main>
      </div>
    );
  }
}

export default App;
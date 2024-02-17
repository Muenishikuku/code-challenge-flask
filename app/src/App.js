import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import Restaurants from './Components/Restaurants';
import Pizzas from './Components/Pizzas';
import Header from './Components/Header';
import RestPizaPost from './Components/RestPizaPost';
import ResPiz from './Components/ResPiz';
import './App.css';

function App() {
    let [restaurants, setRestaurants] = useState([]);
    let [pizzas, setPizzas] = useState([]);
    let [res_piz, setResPiz] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5500/restaurants')
            .then(res => res.json())
            .then(data => setRestaurants(data))
            .catch(error => console.error('Error fetching restaurants:', error));
    }, []);

    useEffect(() => {
        fetch('http://127.0.0.1:5500/pizzas')
            .then(res => res.json())
            .then(data => setPizzas(data))
            .catch(error => console.error('Error fetching pizzas:', error));
    }, []);

    useEffect(() => {
        fetch('http://127.0.0.1:5500/restaurant_pizzas')
            .then(res => res.json())
            .then(data => setResPiz(data))
            .catch(error => console.error('Error fetching restaurant pizzas:', error));
    }, []);

    return (
        <div className="App">
            <Header />
            <div>
                <img src="https://www.sargento.com/assets/Uploads/Recipe/Image/TuscanChikPizza_010.jpg" alt="NA" />
            </div>
            <Routes>
                <Route path='/pizzas' exact element={<Pizzas pizzas={pizzas} />} />
                <Route path='/restaurants' exact element={<Restaurants restaurants={restaurants} setRestaurants={setRestaurants} />} />
                <Route path='/restaurants_pizzas_post' exact element={<RestPizaPost />} />
                <Route path='/restaurants_pizzas' exact element={<ResPiz res_piz={res_piz} />} />
            </Routes>
        </div>
    );
}

export default App;

import React from 'react'

export default function Pizzas({pizzas}) {
	
	let pizza_list = pizzas.map(pizza => {
		return(
			<div key={pizza.rest_id} className='card m-2 p-2'>
				<h3>{pizza.piz_id}</h3>
				<p>Name: {pizza.name}</p>
				<p>Ingredients: {pizza.ingredients}</p>
			</div>
		)
	})
  	return (
    	<>
			<div>
			<h2>Restaurants</h2>
				<div className='restaurants_list'>
					{pizza_list}
				</div>
			</div>
    	</>
  	)
}
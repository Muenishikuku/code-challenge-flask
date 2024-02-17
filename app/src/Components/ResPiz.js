import React from 'react';

export default function ResPiz({res_piz}) {
	let respiz_list = res_piz.map(respiz => {
		return(
			<div key={respiz.rest_piz_id} className='card m-2 p-2'>
				<h3>{respiz.rest_piz_id}</h3>
				<p>Restaurant: {respiz.restaurant.name}</p>
				<p>Pizza: {respiz.pizza.name}</p>
			</div>
		)
	})

	return (
		<div>
			<h2>Restaurants Pizzas</h2>
			{respiz_list}
		</div>
	)
}

import React, {useState} from 'react';

export default function RestPizaPost() {
	const [inputs, setInputs] = useState({});

  	const handleChange = (event) => {
		let name = event.target.name;
		let value = event.target.value;
    	setInputs(current => ({...current, [name]: value}))
 	}
	console.log(inputs);
	function handleSubmit(e){
		e.preventDefault();
		// e.target.reset();

		fetch('http://127.0.0.1:5500/restaurant_pizzas', {
			method: 'POST',
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(inputs)
		})
		.then(res => res.json())
		.then(data => console.log(''))
	}
	return (
		<div>
			<h2 className=''>Add New Restaurant_Pizza</h2>
			<form onSubmit={handleSubmit}>
				<input type='number' name='price' onChange={handleChange} placeholder='Price...'></input>
				<input type='number' name='pizza_id' onChange={handleChange} placeholder='Pizza ID...'></input>
				<input type="number" name="restaurant_id" onChange={handleChange} placeholder='Restaurant ID'></input>
				<input type='submit'></input>
			</form>
		</div>
	)
}

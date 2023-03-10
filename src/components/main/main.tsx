/**
 * @format
 */

import { Route, Routes } from 'react-router-dom';
import { Calculator } from '../paths/pathWrapper';
import { Home } from '../wrapper';
import { Header } from './components/header/header';

export default function Main() {
	return (
		<main className="main_content">
			<Header />
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/calculator" element={<Calculator />} />
			</Routes>
		</main>
	);
}

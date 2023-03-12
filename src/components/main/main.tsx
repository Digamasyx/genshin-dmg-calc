/**
 * @format
 */

import { Route, Routes, useLocation } from 'react-router-dom';
import { Calculator } from '../paths/pathWrapper';
import { Home } from '../wrapper';
import { Header } from './components/header/header';

export default function Main() {
	const a = useLocation().pathname;
	return (
		<main className="main_content">
			{a === '/' ? '' : <Header />}
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/calculator" element={<Calculator />} />
			</Routes>
		</main>
	);
}

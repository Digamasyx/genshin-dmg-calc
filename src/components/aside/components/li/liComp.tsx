/**
 * @format
 */

import { ReactElement } from 'react';
import { NavLink } from 'react-router-dom';

export function LiComp({ name, to, Svg, elemenClass }: Liprop) {
	if (to === undefined) {
		to = '/';
	}
	return (
		<li className="allLis">
			<NavLink to={to} className={elemenClass.navlink}>
				<span className={elemenClass.svgspan}>{Svg}</span>
				<span className={elemenClass.textspan}>{name}</span>
			</NavLink>
		</li>
	);
}

export function Lispan(props: { name: string; class: string }) {
	return (
		<li className="allLis">
			<span className={props.class}>{props.name}</span>
		</li>
	);
}

interface Liprop {
	name: string;
	to?: string;
	Svg: ReactElement;
	elemenClass: {
		navlink: string;
		svgspan: string;
		textspan: string;
	};
}

/**
 * @format
 */
import React from 'react';
import { NavLink } from 'react-router-dom';
import { LiComp, Lispan } from './components/li/liComp';
import {
	Paimon48,
	HomeSvg,
	CalcOutlineSvg,
	HistorySvg,
	Hourglass,
} from './icon/svgWrapper';

export default function Aside() {
	return (
		<aside className="mainAside">
			<div className="headerDiv">
				<div>
					<NavLink to="/" className="headerLink">
						<Paimon48 className="headerSvg" />
						<span className="headerText">Titulo Criativo</span>
					</NavLink>
				</div>
			</div>

			<div className="asideContent">
				<ul className="asideUl">
					<LiComp
						name="Home"
						to="/"
						Svg={<HomeSvg />}
						elemenClass={{
							navlink: 'liA_1',
							svgspan: 'liA_1_svgSpan',
							textspan: 'liA_1_text',
						}}
					/>

					<Lispan name="Tools" class="liSpan_text" />

					<LiComp
						name="Calculator"
						to="/calculator"
						Svg={<CalcOutlineSvg />}
						elemenClass={{
							navlink: 'liA_2',
							svgspan: 'liA_2_svgSpan',
							textspan: 'liA_2_text',
						}}
					/>

					<LiComp
						name="Artifacts"
						to="/artifacts"
						Svg={<Hourglass />}
						elemenClass={{
							navlink: 'liA_3',
							svgspan: 'liA_3_svgSpan',
							textspan: 'liA_3_text',
						}}
					/>
				</ul>
			</div>
		</aside>
	);
}
